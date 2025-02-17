from flask import Flask, jsonify, request
from flask_cors import CORS
import networkx as nx
import sys
import os

# Ajouter le répertoire parent au PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Graph_Scheduling.Ordonnancement import Ordonnancement
from Graph_Scheduling.FileMemory import FileMemory

app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Sauvegarder temporairement le fichier
        temp_path = os.path.join(os.path.dirname(__file__), 'temp.txt')
        file.save(temp_path)
        
        try:
            # Initialiser l'ordonnancement
            scheduling = Ordonnancement()
            
            # Charger les tâches depuis le fichier temporaire
            tasks = scheduling.load_tasks(temp_path)
            if tasks is None:
                return jsonify({'error': 'Failed to load tasks from file'}), 400
            
            # Créer la matrice d'ordonnancement
            matrix = scheduling.creation_scheduling()
            if matrix is None:
                return jsonify({'error': 'Failed to create scheduling matrix'}), 400
            
            # Vérifier l'absence de circuit
            has_circuit = scheduling.not_circuit_detection(matrix)
            
            # Calculer les rangs
            ranks = scheduling.rank_calculation(matrix)
            
            # Calculer le calendrier et les marges
            calendar_data = scheduling.calendar_margin(matrix)
            
            # Obtenir le chemin critique
            critical_path = scheduling.get_critical_path(matrix)
            
            # Créer le graphe pour la visualisation
            nodes = []
            for task in tasks:
                nodes.append({
                    "id": str(task.numero),
                    "label": str(task.numero),
                    "rank": ranks[task.numero] if task.numero < len(ranks) else 0,
                    "duration": task.duree,
                    "early_date": calendar_data['dates_tot'][task.numero] if task.numero < len(calendar_data['dates_tot']) else None,
                    "late_date": calendar_data['dates_tard'][task.numero] if task.numero < len(calendar_data['dates_tard']) else None,
                    "total_margin": calendar_data['marges'][task.numero] if task.numero < len(calendar_data['marges']) else None,
                    "free_margin": 0  # À calculer si nécessaire
                })
            
            # Ajouter les nœuds α et ω
            nodes.insert(0, {
                "id": "α",
                "label": "α",
                "rank": 0,
                "duration": 0,
                "early_date": calendar_data['dates_tot'][0],
                "late_date": calendar_data['dates_tard'][0],
                "total_margin": calendar_data['marges'][0],
                "free_margin": 0
            })
            nodes.append({
                "id": "ω",
                "label": "ω",
                "rank": max(ranks) if ranks else 0,
                "duration": 0,
                "early_date": calendar_data['dates_tot'][-1],
                "late_date": calendar_data['dates_tard'][-1],
                "total_margin": calendar_data['marges'][-1],
                "free_margin": 0
            })
            
            # Créer les arêtes
            edges = []
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] != '∴':
                        from_id = "α" if i == 0 else str(i)
                        to_id = "ω" if j == len(matrix) - 1 else str(j)
                        edges.append({
                            "from": from_id,
                            "to": to_id,
                            "label": str(matrix[i][j])
                        })
            
            return jsonify({
                'graph': {
                    'nodes': nodes,
                    'edges': edges
                },
                'tasks': [{
                    'numero': task.numero,
                    'duree': task.duree,
                    'contraintes': task.contraintes
                } for task in tasks],
                'matrix': [[str(cell) for cell in row] for row in matrix],
                'ranks': {str(i): r for i, r in enumerate(ranks)},
                'calendar': {
                    'early_dates': calendar_data['dates_tot'],
                    'late_dates': calendar_data['dates_tard'],
                    'total_margins': calendar_data['marges'],
                    'free_margins': [0] * len(calendar_data['marges'])
                },
                'criticalPath': [str(i) for i in critical_path],
                'hasCircuit': has_circuit
            })
            
        finally:
            # Nettoyer le fichier temporaire
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/graph/<int:file_number>', methods=['GET'])
def get_graph_data(file_number):
    try:
        # Initialiser l'ordonnancement
        scheduling = Ordonnancement()
        
        # Charger les tâches
        tasks = scheduling.load_tasks()
        
        # Créer la matrice d'ordonnancement
        matrix = scheduling.creation_scheduling()
        
        # Vérifier l'absence de circuit
        has_circuit = scheduling.not_circuit_detection(matrix)
        
        # Calculer les rangs
        ranks = scheduling.rank_calculation(matrix)
        
        # Calculer le calendrier et les marges
        calendar_data = scheduling.calendar_margin(matrix)
        
        # Obtenir le chemin critique
        critical_path = scheduling.get_critical_path(matrix)
        
        # Créer le graphe pour la visualisation
        G = nx.DiGraph()
        
        # Ajouter les nœuds
        nodes = []
        for task in tasks:
            nodes.append({
                "id": str(task.numero),
                "label": str(task.numero),
                "rank": task.rank,
                "duration": task.duree,
                "early_date": task.early_date,
                "late_date": task.late_date,
                "total_margin": task.marge_tot,
                "free_margin": task.marge_libre
            })
        
        # Ajouter les arcs
        edges = []
        for task in tasks:
            for constraint in task.contraintes:
                for pred_task in tasks:
                    if pred_task.numero == constraint:
                        edges.append({
                            "from": str(constraint),
                            "to": str(task.numero),
                            "label": str(pred_task.duree),
                            "value": pred_task.duree
                        })
        
        # Ajouter les nœuds α et ω
        nodes.insert(0, {"id": "α", "label": "α", "rank": 0})
        nodes.append({"id": "ω", "label": "ω", "rank": max(task.rank for task in tasks) + 1})
        
        # Ajouter les arcs depuis α et vers ω
        for task in tasks:
            if not task.contraintes:
                edges.append({
                    "from": "α",
                    "to": str(task.numero),
                    "label": "0",
                    "value": 0
                })
            
            has_successors = False
            for other_task in tasks:
                if task.numero in other_task.contraintes:
                    has_successors = True
                    break
            if not has_successors:
                edges.append({
                    "from": str(task.numero),
                    "to": "ω",
                    "label": str(task.duree),
                    "value": task.duree
                })
        
        return jsonify({
            "graph": {
                "nodes": nodes,
                "edges": edges
            },
            "tasks": [{
                'numero': task.numero,
                'duree': task.duree,
                'contraintes': task.contraintes
            } for task in tasks],
            'matrix': [[str(cell) for cell in row] for row in matrix],
            "ranks": [{"task": str(task.numero), "rank": task.rank} for task in tasks],
            "calendar": [
                {
                    "task": str(task.numero),
                    "early_date": task.early_date,
                    "late_date": task.late_date,
                    "total_margin": task.marge_tot,
                    "free_margin": task.marge_libre
                }
                for task in tasks
            ],
            "criticalPath": critical_path,
            "hasCircuit": has_circuit
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

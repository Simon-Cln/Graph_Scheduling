import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore, Style, init, deinit

from .FileMemory import FileMemory

filememory = FileMemory()
init()

class Task:
    def __init__(self, numero, duree, contraintes):
        self.numero = numero
        self.duree = duree
        self.contraintes = contraintes
        self.early_date = None
        self.late_date = None
        self.marge_tot = None
        self.marge_libre = None
        self.successors = []
        self.rank = None

class Ordonnancement:
    def __init__(self):
        self.tasks = []
        self.early_date = None
        self.late_date = None

    def load_tasks(self, file_path=None):
        tasks_data = filememory.file_reading(file_path)
        if tasks_data is None:
            return None
            
        self.tasks = []
        for task_data in tasks_data:
            task = Task(
                task_data["numero"],
                task_data["duree"],
                task_data["contraintes"]
            )
            self.tasks.append(task)
        return self.tasks

    def creation_scheduling(self):
        if not self.tasks:
            return None

        N = max(task.numero for task in self.tasks)
        nb_sommets = N + 2  # +2 pour α et ω
        taches = self.tasks
        nb_arcs = 0

        # Arcs depuis α
        for tache in taches:
            if not tache.contraintes:
                nb_arcs += 1

        # Arcs entre tâches
        for tache in taches:
            nb_arcs += len(tache.contraintes)

        # Arcs vers ω
        for tache in taches:
            has_successeurs = False
            for autre_tache in taches:
                if tache.numero in autre_tache.contraintes:
                    has_successeurs = True
                    break
            if not has_successeurs:
                nb_arcs += 1

        # Création de la matrice des valeurs
        valeurs = [["∴" for _ in range(nb_sommets)] for _ in range(nb_sommets)]
        
        # Arcs depuis α
        for tache in taches:
            if not tache.contraintes:
                valeurs[0][tache.numero] = 0

        # Arcs entre tâches
        for tache in taches:
            for contrainte in tache.contraintes:
                duree = 0
                for predecesseur in taches:
                    if predecesseur.numero == contrainte:
                        duree = predecesseur.duree
                        break
                valeurs[contrainte][tache.numero] = duree

        # Arcs vers ω
        for tache in taches:
            has_successeurs = False
            for autre_tache in taches:
                if tache.numero in autre_tache.contraintes:
                    has_successeurs = True
                    break
            if not has_successeurs:
                valeurs[tache.numero][N + 1] = tache.duree

        return valeurs

    @staticmethod
    def not_circuit_detection(matrice):
        nb_sommets = len(matrice)
        entrees_totales = []
        points_entree = []

        # Trouver les points d'entrée initiaux
        for i in range(nb_sommets):
            est_point_entree = True
            for j in range(nb_sommets):
                if matrice[j][i] != '∴':
                    est_point_entree = False
                    break
            if est_point_entree:
                points_entree.append(i)
                entrees_totales.append(i)

        # Éliminer les points d'entrée et leurs arcs
        matrice_copie = [ligne[:] for ligne in matrice]
        while points_entree:
            point = points_entree.pop(0)
            
            # Supprimer les arcs sortants
            for j in range(nb_sommets):
                if matrice_copie[point][j] != '∴':
                    matrice_copie[point][j] = '∴'
            
            # Chercher de nouveaux points d'entrée
            for i in range(nb_sommets):
                if i not in entrees_totales:
                    est_point_entree = True
                    for j in range(nb_sommets):
                        if matrice_copie[j][i] != '∴':
                            est_point_entree = False
                            break
                    if est_point_entree:
                        points_entree.append(i)
                        entrees_totales.append(i)

        # Vérifier s'il reste des arcs
        for i in range(nb_sommets):
            for j in range(nb_sommets):
                if matrice_copie[i][j] != '∴':
                    return True

        return False

    def rank_calculation(self, matrice):
        nb_sommets = len(matrice)
        rangs = [0] * nb_sommets
        matrice_copie = [ligne[:] for ligne in matrice]
        sommets_traites = set()

        while len(sommets_traites) < nb_sommets:
            # Trouver les points d'entrée
            for i in range(nb_sommets):
                if i not in sommets_traites:
                    est_point_entree = True
                    for j in range(nb_sommets):
                        if matrice_copie[j][i] != '∴':
                            est_point_entree = False
                            break
                    if est_point_entree:
                        # Calculer le rang
                        rang_max = 0
                        for j in range(nb_sommets):
                            if matrice[j][i] != '∴':
                                rang_max = max(rang_max, rangs[j] + 1)
                        rangs[i] = rang_max
                        sommets_traites.add(i)
                        
                        # Supprimer les arcs sortants
                        for j in range(nb_sommets):
                            matrice_copie[i][j] = '∴'

        return rangs

    def calendar_margin(self, matrice):
        nb_sommets = len(matrice)
        dates_tot = [0] * nb_sommets
        dates_tard = [float('inf')] * nb_sommets
        marges = [0] * nb_sommets
        
        # Calcul des dates au plus tôt
        for i in range(nb_sommets):
            for j in range(nb_sommets):
                if matrice[i][j] != '∴':
                    dates_tot[j] = max(dates_tot[j], dates_tot[i] + int(matrice[i][j]))
        
        # Date de fin au plus tard = date de fin au plus tôt
        dates_tard[-1] = dates_tot[-1]
        
        # Calcul des dates au plus tard
        for i in range(nb_sommets - 2, -1, -1):
            min_date = float('inf')
            for j in range(nb_sommets):
                if matrice[i][j] != '∴':
                    min_date = min(min_date, dates_tard[j] - int(matrice[i][j]))
            dates_tard[i] = min_date if min_date != float('inf') else dates_tot[i]
        
        # Calcul des marges
        for i in range(nb_sommets):
            marges[i] = dates_tard[i] - dates_tot[i]
        
        return {
            'dates_tot': dates_tot,
            'dates_tard': dates_tard,
            'marges': marges
        }

    def get_critical_path(self, matrice):
        calendar_data = self.calendar_margin(matrice)
        critical_path = []
        current = 0  # Start from α
        
        while current < len(matrice):
            critical_path.append(current)
            next_node = None
            for j in range(len(matrice)):
                if (matrice[current][j] != '∴' and 
                    calendar_data['dates_tot'][j] == calendar_data['dates_tard'][j]):
                    next_node = j
                    break
            if next_node is None:
                break
            current = next_node
            
        return critical_path

    def display_critical_path(self, matrice):
        critical_path = self.get_critical_path(matrice)
        return critical_path

    def show_graph(self):
        # On crée un DiGraph
        G = nx.DiGraph()
        # Ajouter α et ω comme noeuds
        G.add_node("α")
        G.add_node("ω")

        # Pour chaque tâche sans contrainte => arc alpha->tache
        for tache in self.tasks:
            if not tache.contraintes:
                G.add_edge("α", str(tache.numero), weight=0)

        # Pour chaque tache, on ajoute arc (contrainte->tache) de poids = durée(contrainte)
        for tache in self.tasks:
            for c in tache.contraintes:
                # chercher durée de c
                duree_c = None
                for t in self.tasks:
                    if t.numero == c:
                        duree_c = t.duree
                        break
                if duree_c is not None:
                    G.add_edge(str(c), str(tache.numero), weight=duree_c)

        # Pour les tâches sans successeur => tache->ω de poids = durée(tache)
        for tache in self.tasks:
            has_successor = False
            for autre in self.tasks:
                if tache.numero in autre.contraintes:
                    has_successor = True
                    break
            if not has_successor:
                G.add_edge(str(tache.numero), "ω", weight=tache.duree)

        pos = nx.spring_layout(G, seed=42, k=2, iterations=50)
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="#A0CBE2", arrowsize=20)

        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        plt.title("Graphe d'Ordonnancement")
        plt.show()

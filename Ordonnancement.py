import FileMemory


class Ordonnancement:
    def creation_scheduling(self):
        taches = FileMemory.FileMemory.file_reading(self)
        N = len(taches)
        nb_sommets = N + 2
        # Afficher le graphe sous forme de matrice
        nb_arcs = 0

        print("* Création du graphe d’ordonnancement :")

        # Ajout des arcs depuis le sommet de départ a
        for tache in taches:
            if tache["numero"] == 1: # tache[numero] parcourt la premiere ligne du fichier (les sommets ou numéros de tache)
                nb_arcs += 1
                print(f"a -> {tache['numero']} = 0")

                # on fait pareil sauf que c'est pour les taches suivantes
                for tache in taches:
                    if not tache["contraintes"]:
                        nb_arcs += 1
                        print(f"0 -> {tache['numero']} = 0")

        # Ajout des arcs entre les tâches
        for tache in taches:
            # Ajouter les arcs pour chaque contrainte (ou prédecesseur) de la tâche
            for contrainte in tache["contraintes"]:
                nb_arcs += 1
                duree = 0
                for predecesseur in taches:
                    if predecesseur["numero"] == contrainte:
                        duree = predecesseur["duree"]
                        break
                print(f"{contrainte} -> {tache['numero']} = {duree}")


        # Ajout de l'arc entre le sommet de fin w et le sommet de départ a
        for tache in taches:
            if tache["numero"] == N:
                duree = 0
                for predecesseur in taches:
                    if predecesseur["numero"] == tache["contraintes"][0]:
                        duree = predecesseur["duree"]
                        break
                nb_arcs += 1
                print(f"{tache['numero']} -> {tache['numero'] + 1}  = {tache['duree']}")

        # Affichage du nombre de sommets et d'arcs
        print(f"{nb_sommets} sommets")
        print(f"{nb_arcs} arcs")

        valeurs = [["*" for _ in range(nb_sommets)] for _ in range(nb_sommets)]

        # Ajout des arcs depuis le sommet de départ a
        for tache in taches:
            if tache["numero"] == 1:
                valeurs[0][1] = 0

                # Ajout des arcs vers le sommet de fin w
                for tache in taches:
                    if not tache["contraintes"]:
                        valeurs[0][tache["numero"]] = 0

        # Ajout des arcs entre les tâches
        for tache in taches:
            # Ajouter les arcs pour chaque contrainte de la tâche
            for contrainte in tache["contraintes"]:
                duree = 0
                for predecesseur in taches:
                    if predecesseur["numero"] == contrainte:
                        duree = predecesseur["duree"]
                        break
                valeurs[contrainte][tache["numero"]] = str(duree)

        # Ajout de l'arc entre le sommet de fin w et le sommet de départ a
        for tache in taches:
            if tache["numero"] == N:
                duree = 0
                for predecesseur in taches:
                    if predecesseur["numero"] == tache["contraintes"][0]:
                        duree = predecesseur["duree"]
                        break
                valeurs[tache["numero"]][N + 1] = str(tache["duree"])


        # Affichage de la matrice des valeurs
        entetes = [""] + [str(i) for i in range(N + 1)] + [str(N+1)]
        print("* Matrice des valeurs")
        print("\t".join(entetes))
        for i in range(nb_sommets):
            ligne = [str(i)]
            for j in range(nb_sommets):
                ligne.append(str(valeurs[i][j]))
            print("\t".join(ligne))

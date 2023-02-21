import FileMemory
import time

class Ordonnancement:

    def creation_scheduling(self):
        BLUE = '\033[34m'
        RESET = '\033[0m'
        taches = FileMemory.FileMemory.file_reading(self)
        N = len(taches)
        nb_sommets = N + 2
        # Afficher le graphe sous forme de matrice
        nb_arcs = 0

        print(BLUE + "\n* Création du graphe d’ordonnancement :" + RESET)

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
        return valeurs

    def circuit_detection(matrice):
        # Définition des codes d'échappement ANSI
        GREEN = '\033[32m'
        RESET = '\033[0m'
        BLUE = '\033[34m'

        print(BLUE + "\n* Méthode d'élimination des points d'entrée\n* Détection de circuit en cours\n" + RESET)

        entrees_totales = []
        # Recherche des points d'entrée
        points_entree = []
        for i in range(len(matrice)):
            est_point_entree = True
            for j in range(len(matrice)):
                if matrice[j][i] != '*':
                    est_point_entree = False
                    break
            if est_point_entree:
                points_entree.append(i)
                entrees_totales.append(i)
        print("Point(s) d'entrée :",", ".join(str(x) for x in points_entree) )


        # Boucle principale de détection de circuit
        while points_entree:

            import time

            WAIT_TIME = 0.4  # temps d'attente en secondes

            while points_entree:

                # Suppression des points d'entrée et nouveaux points d'entrée créés
                for i in points_entree:
                    for j in range(len(matrice)):
                        matrice[i][j] = '*'
                    # Animation d'attente
                    print("Suppression des points d'entrée en cours", end="")
                    for i in range(3):
                        print(".", end="")
                        time.sleep(WAIT_TIME)
                    print("\r   \r", end="")

                sommets = []
                for i in range(len(matrice)):
                    if i not in sommets and i not in points_entree and i not in entrees_totales:
                        sommets.append(i)
                    for j in range(len(matrice)):
                        if matrice[i][j] != '*' and j not in points_entree and i not in sommets:
                            sommets.append(i)
                print("Sommets restants :", ", ".join(str(x) for x in sommets))

                # Recherche des nouveaux points d'entrée
                nouveaux_points_entree = []
                for i in sommets:
                    est_point_entree = True
                    for j in range(len(matrice)):
                        if matrice[j][i] != '*':
                            est_point_entree = False
                            break
                    if est_point_entree:
                        nouveaux_points_entree.append(i)
                        entrees_totales.append(i)
                print("Nouveaux Points d'entrée :", ", ".join(str(x) for x in nouveaux_points_entree))

                # Vérification d'arcs à valeur négative
                for i in range(len(matrice)):
                    for j in range(len(matrice)):
                        if matrice[i][j] != '*' and int(matrice[i][j]) < 0:
                            print("-> Il y a au moins un arc à valeur négative")
                            return False

                if not nouveaux_points_entree:
                    print(GREEN + "\n-> Il n'y a pas de circuit" + RESET)
                    # S'il ne reste plus de sommets, le graphe n'a pas de circuit

                points_entree = nouveaux_points_entree

            print(GREEN + "-> Il n'y a pas d'arcs négatifs !\n-> C'est un graphe d'ordonnancement !" + RESET + "\n")
            return True





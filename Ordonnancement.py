# -*- coding: utf-8 -*-
from Display import Display
from FileMemory import FileMemory
import time
from tqdm import tqdm
from colorama import Fore, Style, init, deinit
import re
import prettytable as pt
filememory = FileMemory()
display = Display()
init()
# Définition des constantes
N = 13
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
RED = Fore.RED

class Task:
    def __init__(self, numero, duree, contraintes):
        self.numero = numero
        self.duree = duree
        self.contraintes = contraintes
        self.early_date = None
        self.late_date = None
        self.marge_tot = None
        self.marge_libre = None
        self.successors = []  # définir l'attribut successors à une liste vide par défaut
        self.rank = None
        # définir l'attribut predecessors à une liste vide par défaut


class Ordonnancement:

    def __init__(self):
        self.tasks = self.load_tasks()
        self.early_date = None
        self.late_date = None

    def load_tasks(self):
        file_data = filememory.file_reading()
        tasks = []
        for task_data in file_data:
            task = Task(
                numero=task_data["numero"],
                duree=task_data["duree"],
                contraintes=task_data["contraintes"],
            )
            tasks.append(task)

        self.tasks = tasks
    def creation_scheduling(self):
        taches = self.tasks
        BLUE = '\033[34m'
        RESET = '\033[0m'
        RED = '\033[31m'
        N = len(taches)
        nb_sommets = N + 2
        # Afficher le graphe sous forme de matrice
        nb_arcs = 0

        print(BLUE + "\n* Création du graphe d’ordonnancement :" + RESET)

        # Ajout des arcs depuis le sommet de départ a
        for tache in taches: #tache est une ligne
            if tache.numero == 1: # tache[numero] parcourt la premiere ligne du fichier (les sommets ou numéros de tache)

                # on fait pareil sauf que c'est pour les taches suivantes
                for tache in taches:
                    if not tache.contraintes: #successeur = contrainte
                        nb_arcs += 1
                        print(f"α -> {tache.numero} = 0")



        # Ajout des arcs entre les tâches
        for tache in taches:
            # Ajouter les arcs pour chaque contrainte (ou prédecesseur) de la tâche
            for contrainte in (tache.contraintes):
                nb_arcs += 1
                duree = 0
                for predecesseur in taches:
                    if predecesseur.numero == contrainte:
                        duree = predecesseur.duree
                        break
                print(f"{contrainte} -> {tache.numero} = {duree}")


        for tache in taches:
            has_successeurs = False
            for autre_tache in taches:
                if tache.numero in autre_tache.contraintes:
                    has_successeurs = True
                    break
            if not has_successeurs:
                nb_arcs += 1
                print(f"{tache.numero} -> {'ω'}  = {tache.duree}")

        # Affichage du nombre de sommets et d'arcs
        print(f"{nb_sommets} sommets")
        print(f"{nb_arcs} arcs")

        #●
        # ∴ ∞ ∇ ∑ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ ⋣ ⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ⌀ ⌁ ⌂
        # Création de la matrice des valeurs
        valeurs = [["∴" for _ in range(nb_sommets)] for _ in range(nb_sommets)]
        # Ajout des arcs vers le sommet de fin w
        for tache in taches:
            if not tache.contraintes:
                valeurs[0][tache.numero] = Style.BRIGHT + Fore.LIGHTGREEN_EX + str(0) + Style.RESET_ALL + Fore.RESET

        # Ajout des arcs entre les tâches
        for tache in taches:
            # Ajouter les arcs pour chaque contrainte de la tâche
            for contrainte in tache.contraintes:
                duree = 0
                for predecesseur in taches:
                    if predecesseur.numero == contrainte:
                        duree = predecesseur.duree
                        break
                valeurs[contrainte][tache.numero] = Style.BRIGHT + Fore.LIGHTGREEN_EX + str(duree) + Style.RESET_ALL + Fore.RESET

        # Ajout de l'arc entre le sommet de fin w
        for tache in taches:
            has_successeurs = False
            for autre_tache in taches:
                if tache.numero in autre_tache.contraintes:
                    has_successeurs = True
                    break
            if not has_successeurs:
                valeurs[tache.numero][N + 1] = Style.BRIGHT + Fore.LIGHTGREEN_EX + str(tache.duree) + Style.RESET_ALL + Fore.RESET



        # Affichage de la matrice des valeurs
        entetes = [""] + [BLUE + "α" + RESET]+[str(i) for i in range(1, N + 1)]+[RED+'ω' + RESET]

        print(BLUE + "\n* Matrice des valeurs\n" + RESET)
        print("\t".join(entetes))
        for i in range(nb_sommets):

            ligne = [str(i)]
            if i == 0:
                ligne[0] = (BLUE +"α"+RESET)
            elif i == N + 1:
                ligne[0] = (RED+"ω"+RESET)

            for j in range(nb_sommets):
                ligne.append(str(valeurs[i][j]))
            print("\t".join(ligne))
            time.sleep(0.4)
        return valeurs

    def not_circuit_detection(matrice):
        # Définition des codes d'échappement ANSI
        GREEN = '\033[32m'
        RESET = '\033[0m'
        BLUE = '\033[34m'
        RED = '\033[31m'

        print(BLUE + "\n* Méthode d'élimination des points d'entrée\n* Détection de circuit en cours\n" + RESET)
        nb_sommets = len(matrice)
        entrees_totales = []
        # Recherche des points d'entrée
        points_entree = []
        for i in tqdm(range(len(matrice))):
            est_point_entree = True
            for j in range(len(matrice)):
                if matrice[j][i] != '∴':
                    est_point_entree = False
                    break
            if est_point_entree:
                if i == 0:
                    points_entree.append('α')
                else:
                    points_entree.append(i)
                entrees_totales.append(i)
        print("Point(s) d'entrée :", ", ".join(str(x) for x in points_entree))

        # Remplacement de 'α' et 'ω' par 0 et len(matrice) - 1
        for i, point in enumerate(points_entree):
            if point == 'α':
                points_entree[i] = 0



        # Boucle principale de détection de circuit
        while points_entree:

            WAIT_TIME = 0.3  # temps d'attente en secondes

            while points_entree:
                # Suppression des points d'entrée et nouveaux points d'entrée créés
                for i in points_entree:
                    for j in range(len(matrice)):
                        matrice[i][j] = '∴'
                    # Animation d'attente
                    print("Suppression des points d'entrée en cours", end="")
                    for i in range(3):
                        print(".", end="")
                        time.sleep(WAIT_TIME)
                    print("\r   \r", end="")

                # Recherche des sommets restants
                sommets = []
                for i in range(len(matrice)):
                    if i not in sommets and i not in points_entree and i not in entrees_totales:
                        sommets.append(i)
                        if i == len(matrice) - 1:
                            sommets[-1] = 'ω'
                    for j in range(len(matrice)):
                        if matrice[i][j] != '∴' and j not in points_entree and i not in sommets:
                            sommets.append(i)
                            if j == len(matrice) - 1:
                                sommets[-1] = 'ω'
                print("Sommets restants :", ", ".join(str(x) for x in sommets))
                for i, sommet in enumerate(sommets):
                    if sommet == 'ω':
                        sommets[i] = len(matrice) - 1


                # Recherche des nouveaux points d'entrée
                nouveaux_points_entree = []
                for i in sommets:
                    est_point_entree = True
                    for j in range(len(matrice)):
                        if matrice[j][i] != '∴':
                            est_point_entree = False
                            break
                    if est_point_entree:
                        nouveaux_points_entree.append(i)
                        entrees_totales.append(i)
                        if i == len(matrice) - 1:
                            nouveaux_points_entree[-1] = 'ω'




                if len(nouveaux_points_entree) > 0:
                    print("Nouveaux Points d'entrée :", ", ".join(str(x) for x in nouveaux_points_entree))
                else:
                    print("Nouveaux Points d'entrée :", RED + "Aucun" + RESET)
                for i, sommet in enumerate(nouveaux_points_entree):
                    if sommet == 'ω':
                        nouveaux_points_entree[i] = len(matrice) - 1

                # Vérification d'arcs à valeur négative
                for i in range(len(matrice)):
                    for j in range(len(matrice)):
                        if str(matrice[i][j]) != '∴' and str(matrice[i][j]).__contains__('-'):
                            print(Style.BRIGHT + Fore.LIGHTRED_EX +"\n-> Il y a au moins un arc à valeur négative\n" + Style.BRIGHT + Fore.LIGHTRED_EX)
                            display.launch()
                            return False

                if not nouveaux_points_entree and len(sommets) > 0 :
                    print(Style.BRIGHT + Fore.LIGHTRED_EX + "\n-> Il y a donc un circuit, vous ne pouvez pas aller plus loin :( !\n" + Style.BRIGHT + Fore.LIGHTRED_EX )
                    # S'il ne reste plus de sommets, le graphe n'a pas de circuit
                    display.launch()
                    return False


                points_entree = nouveaux_points_entree

            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "\n\n-> Il n'y a pas d'arcs négatifs ni de circuit !\n-> C'est un graphe d'ordonnancement !" + Style.BRIGHT + Fore.LIGHTRED_EX + "\n")
            return True

    def rank_calculation(matrice):
        matrice_copy = [row[:] for row in matrice]  # faire une copie de la matrice

        if not Ordonnancement.not_circuit_detection(matrice_copy):
            print(Style.BRIGHT + Fore.LIGHTRED_EX +"Ce n'est donc pas un graphe d'ordonnancement :(\n"+ Style.BRIGHT + Fore.LIGHTRED_EX)
            return False
        else:
            n = len(matrice)
            degres = [0] * n
            for i in range(n):
                for j in range(n):
                    if matrice[i][j] != '∴':
                        degres[j] += 1

            rangs = [0] * n
            a_traiter = [i for i in range(n) if degres[i] == 0]

            k = 0
            while len(a_traiter) > 0:
                a_traiter_suivant = []
                for i in a_traiter:
                    rangs[i] = k
                    for j in range(n):
                        if matrice[i][j] != '∴':
                            degres[j] -= 1
                            if degres[j] == 0:
                                a_traiter_suivant.append(j)
                a_traiter = a_traiter_suivant
                k += 1

            print(Style.BRIGHT + Fore.LIGHTGREEN_EX+ "CALCUL DES RANGS EN COURS\n" + Style.BRIGHT + Fore.LIGHTGREEN_EX)
            for i in range(3):
                print(".", end="")
                time.sleep(0.4)
            print("\r   \r", end="")
            init()
            print('╒═══════╤═══════╕')
            print('│ Tache │ Rang  │')
            print('╞═══════╪═══════╡')
            for i in range(n):
                if i == 0:
                    tache = 'α'
                elif i == n - 1:
                    tache = 'ω'
                else:
                    tache = i
                print('│{:^7}│{:^7}│'.format(tache, rangs[i]))
                time.sleep(0.35)
                if i < n - 1:
                    print('├───────┼───────┤')
            print('╘═══════╧═══════╛')

            return rangs

    def remove_escape_chars(matrice):
        new_matrice = []
        for ligne in matrice:
            if isinstance(ligne, str):
                new_ligne = re.sub('\x1b\[[0-9;]*m', '', ligne)
            else:
                new_ligne = []
                for element in ligne:
                    new_element = re.sub('\x1b\[[0-9;]*m', '', element)
                    new_ligne.append(new_element)
            new_matrice.append(new_ligne)
        return new_matrice

    def calendar_margin(matrice):

        new_matrice = Ordonnancement.remove_escape_chars(matrice)

        Ordonnancement.rank_calculation(new_matrice)

        n = len(new_matrice)
        tot = [0] * n
        for row in new_matrice:
            if row != '∴':
                new_matrice[new_matrice.index(row)] = [int(x) if x.isdigit() else 0 for x in row]

        # calcul des dates au plus tôt
        earlydate = [0] * n
        for j, task in enumerate(new_matrice):
            for i, duration in enumerate(task):
                if duration != 0:
                    if earlydate[i] == 0:
                        earlydate[i] = duration + earlydate[j]
                    else:
                        earlydate[i] = max(earlydate[i], earlydate[j] + duration)

        #calcul des dates au plus tard + marges
        late_date = [earlydate[-1]] * n
        margin = [0] * n

        for i in range(n - 2, -1, -1):
            for j in range(n):
                if new_matrice[i][j] != 0:
                    late_date[i] = min(late_date[i], late_date[j] - new_matrice[i][j])
            margin[i] = late_date[i] - earlydate[i]


        # affichage des résultats
        print("\nCALCUL DES CALENDRIERS ET DES MARGES EN COURS ")
        for i in range(3):
            print(".", end="")
            time.sleep(0.4)

        print("\n")
        print('╒═══════╤═══════╤═══════╤═══════╕')
        print('│ Tache │  Tot  │ Tard  │ Marge │')
        print('╞═══════╪═══════╪═══════╪═══════╡')
        for i in range(n):
            if i == 0:
                tache = "α"
                late_date[i] = 0
                margin[i] = 0
            elif i == n - 1:
                tache = "ω"
            else:
                tache = str(i)
            print('│{:^7}│{:^7}│{:^7}│{:^7}│'.format(tache, earlydate[i], late_date[i], margin[i]))

            time.sleep(0.35)
            if i < n - 1:
                print('├───────┼───────┼───────┼───────┤')
        print('╘═══════╧═══════╧═══════╧═══════╛')

        return (tache, earlydate, late_date, margin)

    def display_critical_path(matrice):


        i, tot, tard, marges = Ordonnancement.calendar_margin(matrice)

        crit_path = []
        for i in range(len(marges)):
            if marges[i] == 0:
                crit_path.append(i)

        if len(crit_path) > 0:
            if crit_path[0] == 0:
                crit_path[0] = "α"
            if crit_path[-1] == len(marges) - 1:
                crit_path[-1] = "ω"

            print(RED + "Le chemin critique est :" + RESET)
            print(" ❯ ".join(str(task) for task in crit_path))
        else:
            print("Il n'y a pas de chemin critique.")






























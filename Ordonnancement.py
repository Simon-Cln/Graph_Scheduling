import FileMemory
import time
from tqdm import tqdm
from colorama import Fore, Style, init, deinit
import re

init()
# Définition des constantes
N = 13
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
RED = Fore.RED
class Ordonnancement:
    def creation_scheduling(self):
        taches = FileMemory.FileMemory.file_reading(self)
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
            if tache["numero"] == 1: # tache[numero] parcourt la premiere ligne du fichier (les sommets ou numéros de tache)

                # on fait pareil sauf que c'est pour les taches suivantes
                for tache in taches:
                    if not tache["contraintes"]: #successeur = contrainte
                        nb_arcs += 1
                        print(f"α -> {tache['numero']} = 0")



        # Ajout des arcs entre les tâches
        for tache in taches:
            # Ajouter les arcs pour chaque contrainte (ou prédecesseur) de la tâche
            for contrainte in (tache["contraintes"]):
                nb_arcs += 1
                duree = 0
                for predecesseur in taches:
                    if predecesseur["numero"] == contrainte:
                        duree = predecesseur["duree"]
                        break
                print(f"{contrainte} -> {tache['numero']} = {duree}")


        for tache in taches:
            has_successeurs = False
            for autre_tache in taches:
                if tache["numero"] in autre_tache["contraintes"]:
                    has_successeurs = True
                    break
            if not has_successeurs:
                nb_arcs += 1
                print(f"{tache['numero']} -> {'ω'}  = {tache['duree']}")

        # Affichage du nombre de sommets et d'arcs
        print(f"{nb_sommets} sommets")
        print(f"{nb_arcs} arcs")

        #●
        # ∴ ∞ ∇ ∑ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ ⋣ ⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ⌀ ⌁ ⌂
        # Création de la matrice des valeurs
        valeurs = [["∴" for _ in range(nb_sommets)] for _ in range(nb_sommets)]
        # Ajout des arcs vers le sommet de fin w
        for tache in taches:
            if not tache["contraintes"]:
                valeurs[0][tache["numero"]] = Style.BRIGHT + Fore.LIGHTGREEN_EX + str(0) + Style.RESET_ALL + Fore.RESET

        # Ajout des arcs entre les tâches
        for tache in taches:
            # Ajouter les arcs pour chaque contrainte de la tâche
            for contrainte in tache["contraintes"]:
                duree = 0
                for predecesseur in taches:
                    if predecesseur["numero"] == contrainte:
                        duree = predecesseur["duree"]
                        break
                valeurs[contrainte][tache["numero"]] = Style.BRIGHT + Fore.LIGHTGREEN_EX + str(duree) + Style.RESET_ALL + Fore.RESET

        # Ajout de l'arc entre le sommet de fin w
        for tache in taches:
            has_successeurs = False
            for autre_tache in taches:
                if tache["numero"] in autre_tache["contraintes"]:
                    has_successeurs = True
                    break
            if not has_successeurs:
                valeurs[tache["numero"]][N + 1] = Style.BRIGHT + Fore.LIGHTGREEN_EX + str(tache["duree"]) + Style.RESET_ALL + Fore.RESET



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
                points_entree.append(i)
                entrees_totales.append(i)
        print("Point(s) d'entrée :", ", ".join(str(x) for x in points_entree))

        # Boucle principale de détection de circuit
        while points_entree:

            WAIT_TIME = 0.4  # temps d'attente en secondes

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

                sommets = []
                for i in range(len(matrice)):
                    if i not in sommets and i not in points_entree and i not in entrees_totales:
                        sommets.append(i)
                    for j in range(len(matrice)):
                        if matrice[i][j] != '∴' and j not in points_entree and i not in sommets:
                            sommets.append(i)
                print("Sommets restants :", ", ".join(str(x) for x in sommets))

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
                        print("Nouveaux Points d'entrée :", ", ".join(str(x) for x in nouveaux_points_entree))

                if len(nouveaux_points_entree) == 0:
                            print("Nouveaux Points d'entrée :", RED + "Aucun" + RESET)





                # Vérification d'arcs à valeur négative
                for i in range(len(matrice)):
                    for j in range(len(matrice)):
                        if str(matrice[i][j]) != '∴' and int(re.search(r'\d+', str(matrice[i][j])).group()) < 0:
                            print(RED+"\n-> Il y a au moins un arc à valeur négative"+RESET)
                            return False


                if not nouveaux_points_entree:
                    print(Style.BRIGHT + Fore.LIGHTRED_EX + "\n-> Il y a donc un circuit !" + Style.RESET_ALL + Fore.RESET)
                    # S'il ne reste plus de sommets, le graphe n'a pas de circuit
                    return False

                points_entree = nouveaux_points_entree

            print(GREEN + "-> Il n'y a pas d'arcs négatifs !\n-> C'est un graphe d'ordonnancement !" + RESET + "\n")
            return True

    def rank_calculation(matrice):
        matrice_copy = [row[:] for row in matrice]  # faire une copie de la matrice

        if not Ordonnancement.not_circuit_detection(matrice_copy):
            print("Ce n'est donc pas un graphe d'ordonnancement :(")
            return
        else:
            n = len(matrice)
            degres = [0] * n
            for i in range(n):
                for j in range(n):
                    if matrice[i][j] != '*':
                        degres[j] += 1

            rangs = [0] * n
            a_traiter = [i for i in range(n) if degres[i] == 0]

            k = 0
            while len(a_traiter) > 0:
                a_traiter_suivant = []
                for i in a_traiter:
                    rangs[i] = k
                    for j in range(n):
                        if matrice[i][j] != '*':
                            degres[j] -= 1
                            if degres[j] == 0:
                                a_traiter_suivant.append(j)
                a_traiter = a_traiter_suivant
                k += 1
            return rangs

    def calendrier_plus_tot(matrice, rangs):
        n = len(matrice)
        durees = [0] * n
        for i in range(n):
            durees[i] = max([durees[j] + matrice[j][i] for j in range(n) if matrice[j][i] != '*'])
        dates_plus_tot = [0] * n
        for i in range(n):
            dates_plus_tot[i] = durees[i] - rangs[i]
        return dates_plus_tot

    def afficher_calendrier_plus_tot(matrice):
        rangs = Ordonnancement.rank_calculation(matrice)
        dates_plus_tot = Ordonnancement.calendrier_plus_tot(matrice, rangs)
        print("Calendrier au plus tôt :")
        for i in range(len(matrice)):
            print("Tâche {}: date de début = {}".format(i + 1, dates_plus_tot[i]))














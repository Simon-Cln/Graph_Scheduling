import glob

class FileMemory:

    def file_reading(self):
        file_txt = glob.glob("*.txt")
        # Demander à l'utilisateur de rentrer un numéro de fichier
        while True:
            try:
                num_fichier = int(input("Entrez un numéro de fichier : "))
                break
            except ValueError:
                print("Erreur : le numéro de fichier doit être un entier.")

        # Vérifier si le numéro de fichier est valide
        nb_fichiers = len(file_txt)  # Nombre de fichiers dans l'exemple
        while num_fichier < 1 or num_fichier > nb_fichiers:
            print("Le numéro de fichier est invalide.")
            num_fichier = int(input("Entrez un nouveau numéro de fichier : "))

        # Ouvrir le fichier en mode lecture
        nom_fichier = "file{}.txt".format(num_fichier)
        try:
            with open(nom_fichier, "r") as fichier:
                # Traitement du fichier
                # Initialiser une liste pour stocker les informations des tâches
                taches = []
                # Parcourir le fichier ligne par ligne
                for ligne in fichier:
                    # Diviser la ligne en une liste de nombres
                    elements = ligne.strip().split()
                    # Convertir les éléments de la liste en entiers
                    elements = [int(x) for x in elements]
                    # Stocker les informations de la tâche dans un dictionnaire
                    tache = {"numero": elements[0], "duree": elements[1], "contraintes":  elements[2:]}
                    # Ajouter la tâche à la liste des tâches
                    taches.append(tache)


        except FileNotFoundError:
            print("Le fichier {} n'existe pas.".format(nom_fichier))
        except PermissionError:
            print("Vous n'avez pas les droits d'accès pour lire le fichier {}.".format(nom_fichier))
        except ValueError:
            print("Le format du fichier {} est incorrect.".format(nom_fichier))

        # Tri des taches en fonction de leurs contraintes triées et de leur numéro
        taches.sort(key=lambda tache: (sorted([int(c) for c in tache["contraintes"]]), tache["numero"]))

        # Traitement des taches sans contraintes entrantes en premier

        return taches






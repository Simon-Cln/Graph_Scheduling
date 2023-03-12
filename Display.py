import FileMemory
import Ordonnancement

class Display:

    def launch(self):
        final = Ordonnancement.Ordonnancement
        reponse = 'oui'
        while reponse.lower() != 'non':
            # Demander à l'utilisateur de lancer le programme
            reponse = input("\nVoulez-vous lancer le programme ? (oui/non) ")

            if reponse.lower() == 'oui':
                # Lancer le programme
                print("Programme lancé!")
                final.load_tasks(self)  # Charger les tâches
                final.display_critical_path(final.creation_scheduling(self))
            elif reponse.lower() != 'non':
                # Répéter la demande si la réponse n'est pas valide
                print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")
        print("Programme terminé.")
        exit()


if __name__ == '__main__':
    main = Display()
    main.launch()

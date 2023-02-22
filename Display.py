import FileMemory
import Ordonnancement

class Display:

    def launch(self):
        final = Ordonnancement.Ordonnancement
        reponse = 'oui'
        while reponse.lower() != 'non':
            # Demander à l'utilisateur de lancer le programme
            reponse = input("Voulez-vous lancer le programme ? (oui/non) ")

            if reponse.lower() == 'oui':
                # Lancer le programme
                print("Programme lancé!")
                #Display.display_result(self)
                final.display_ranks(final.creation_scheduling(self))
            elif reponse.lower() != 'non':
                # Répéter la demande si la réponse n'est pas valide
                print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")


if __name__ == '__main__':
    main = Display()
    main.launch()

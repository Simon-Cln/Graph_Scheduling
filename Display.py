import FileMemory
import Ordonnancement



class Display:

    """def display_result(self):
        file_memory = InMemory.FileMemory()  # créer une instance de la classe FileMemory
        tache = file_memory.file_reading()  # appeler la méthode file_reading à partir de l'instance créée
        for i in range(len(tache)):
            print(tache[i])"""


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
                final.creation_scheduling(self)
            elif reponse.lower() != 'non':
                # Répéter la demande si la réponse n'est pas valide
                print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")


if __name__ == '__main__':
    main = Display()
    main.launch()

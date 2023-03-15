import FileMemory
import Ordonnancement
import time
from colorama import Fore, Style, init, deinit

init()
class Display:

    def launch(self):
        final = Ordonnancement.Ordonnancement
        reponse = 'oui'
        while reponse.lower() != 'non':
            # Demander à l'utilisateur de lancer le programme
            reponse = input("\nVoulez-vous lancer le programme ? (oui/non) ")

            if reponse.lower() == 'oui':
                # Lancer le programme avec décompte chargement avec pourcentage et pourcentage en rouge puis orange puis vert
                color = Fore.RED
                '''for i in range(0, 101, 10):
                    print(f"Chargement en cours...{color}{i}%")
                    time.sleep(0.1)'''

                for i in range(0, 101, 10):
                    time.sleep(0.3)
                    print("\r", end="")
                    print("Chargement du programme en cours... {} {}%".format(color, i), end="")
                    if i < 30:
                        color = Fore.RED
                    elif i < 60:
                        color = Fore.YELLOW
                    elif i < 100:
                        color = Fore.GREEN




                print("\nProgramme lancé!")
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

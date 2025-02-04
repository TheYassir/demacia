import json
import sys
sys.path.insert(0, '..')

from utils.afficher_une import affiche_une_tache
from utils.ajout_tache import ajout_tache
from utils.afficher_tout import affiche_tout_tache
from utils.supprimer_tout import supprimer_tout_tache
from utils.supprimer_une import supprime_tache


def main():
    with open('data.json', 'r') as file:
        task = json.load(file)
    while True:
        print("\nTo-Do List")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Afficher une tache")
        print("4. Supprimer une tâche")
        print("5. Supprimer toute les tâches")
        print("6. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == '1':
            affiche_tout_tache(task)
        elif choice == '2':
            tempstask=task
            task=ajout_tache(tempstask)
        elif choice == '3':
            affiche_une_tache(task)
        elif choice == '4':
            tempstask=task
            task=supprime_tache(tempstask)
        elif choice == '5':
            tempstask=task
            task=supprimer_tout_tache(tempstask)
            print ("task =",task)
        elif choice == '6':
            f = open(f'data.json', mode="w")
            f.write(json.dumps(task))
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
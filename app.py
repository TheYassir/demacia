from .utils.afficher_une import affiche_une_tache
from .utils.ajout_tache import ajout_tache
from .utils.afficher_tout import affiche_tout_tache
from .utils.supprimer_tout import supprimer_tout_tache
from .utils.supprimer_une import supprime_tache

task  = ['Tomates','Pain']

def main():
    while True:
        print("\nTo-Do List")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Afficher une tache")
        print("4. Supprimer une tâche")
        print("5. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == '1':
            affiche_tout_tache()
        elif choice == '2':
            ajout_tache()
        elif choice == '3':
            affiche_une_tache()
        elif choice == '4':
            supprime_tache()
        elif choice == '5':
            supprimer_tout_tache()
        elif choice == '6':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
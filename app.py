import os
import affiche_tache

task  = ['Tomates','Pain']

def ajout_tache():
    return 1

def complete_tache():
    return 1

def supprime_tache():
    return 1

def affiche_tache():
     affiche_tache.affiche_tache()

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
            affiche_tache()
        elif choice == '2':
            ajout_tache()
        elif choice == '3':
            complete_tache()
        elif choice == '4':
            supprime_tache()
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
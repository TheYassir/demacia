import os
task =['Tomates', 'Pain']

def affiche_une_tache():
    if not task:
        print ("aucune tache disponible.")
        return
    try :
        index = int(input(f"Entrez l'index de la tâche (0-{len(task)-1}): "))
        if 0 <= index < len(task):
            print(f"Tâche sélectionnée : {task[index]}")
        else:
            print("Index invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
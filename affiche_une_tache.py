import os
# Liste des tâches initiales
task =['Tomates', 'Pain']

def affiche_une_tache():
     # Vérifie si la liste de tâches est vide
    if not task:
        print ("aucune tache disponible.")
        return
    try :
        # Demande à l'utilisateur de saisir un index de tâche
        index = int(input(f"Entrez l'index de la tâche (0-{len(task)-1}): "))
        # Vérifie si l'index est valide
        if 0 <= index < len(task):
            print(f"Tâche sélectionnée : {task[index]}")
        else:
            print("Index invalide.")
    except ValueError:
        # Gère le cas où l'utilisateur entre une valeur non numérique
        print("Veuillez entrer un nombre valide.")
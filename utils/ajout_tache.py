################################
#                              #
#        Par Benjamin          #
#                              #
################################

import os  # Même structure que ton collègue

# Liste des tâches initiales
task = ['Tomates', 'Pain']

def ajout_tache():
    """Ajoute une tâche à la liste."""
    
    nouvelle_tache = input("Entrez la nouvelle tâche : ").strip()

    if not nouvelle_tache:
        print("⚠️ Impossible d'ajouter une tâche vide.")
        return
    
    # Ajoute la tâche à la liste
    task.append(nouvelle_tache)
    print(f"✅ Tâche ajoutée : {nouvelle_tache}")

def ajout_tache(task_list):
    nouvelle_tache = input("Entrez la nouvelle tâche : ").strip()

    if nouvelle_tache:
        task_list.append(nouvelle_tache)
        print(f"✅ Tâche ajoutée : {nouvelle_tache}")
    else:
        print("⚠️ Impossible d'ajouter une tâche vide.")

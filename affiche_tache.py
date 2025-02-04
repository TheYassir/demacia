def affiche_tache():
    
    try:
        from app import task  
    except ImportError:
        task = []  

    if not task:
        print("\n📭 Aucune tâche enregistrée.")
    else:
        print("\n📝 Liste des tâches :")
        for index, t in enumerate(task, start=1):
            print(f"{index}. {t}")

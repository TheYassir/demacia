def affiche_tout_tache(task):

    if not task:
        print("Aucune tâche enregistrée.")
    else:
        print("\n📝 Liste des tâches :")
        for index, t in enumerate(task, start=1):
            print(f"{index}. {t}")



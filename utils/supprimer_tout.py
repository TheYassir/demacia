def supprimer_tout_tache(task):

    try:
        from app import task  
    except ImportError:
        task = []  

    task = []
    print (task)
    print ("Taches supprimées.")
    return task
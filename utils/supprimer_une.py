def supprime_tache(task):

    indice=int(input("Donne un numéro : "))

    indice=indice-1

    del task[indice]

    print("suppression d'une tache")

    return task


def affiche_une_tache(task):

    num=int(input("Donne un numéro : "))
    num=num-1
    print(len(task))

    if num>=0 and num<len(task):
        return print(task[num])
    else:
        return print("Donne un nombre valide")

    
import json

todo_file = "todolist.json"

def load_tasks():
    try:
        with open(todo_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(todo_file, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Tâche ajoutée : {task}")

def remove_task(task):
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"❌ Tâche supprimée : {task}")
    else:
        print("⚠️ Tâche non trouvée.")

def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("📌 Liste des tâches :")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("📭 Aucune tâche pour le moment.")

if __name__ == "__main__":
    while True:
        print("\n1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Lister les tâches")
        print("4. Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            task = input("Entrez la tâche : ")
            add_task(task)
        elif choix == "2":
            task = input("Entrez la tâche à supprimer : ")
            remove_task(task)
        elif choix == "3":
            list_tasks()
        elif choix == "4":
            print("👋 Au revoir !")
            break
        else:
            print("❌ Option invalide, réessayez.")

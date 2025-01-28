#Gestion d'une todolist alimentée par un fichier JSON

import json
import os.path
import argparse

FILE = "todo.json"

#Chargement des données. Si le fichier a déjà été créé, on l'ouvre, sinon on le crée
def load_data():
    if os.path.isfile(FILE):
        with open(FILE, 'r') as file:
            return json.load(file)
    else:
        return {"tasks":[]}

#Sauvegarde des données dans le fichier json
def save_data(data):
    with open("todo.json", "w") as openfile:
        json.dump(data, openfile, indent=4)

#Ajout d'une tâche
def add(task):
    data = load_data() 
    lastid = data['tasks'][-1]['id']
    
    data['tasks'].append({"id": lastid + 1, "task": task, "progression": "Todo"})
        
    save_data(data)

#Liste toutes les tâches
def list():
    data = load_data()
    
    if data['tasks']:
        for task in data['tasks']:
            print(f"{task['id']} - {task['task']} - {task['progression']}")
        
#Met à jour une tâche, retrouvée par son identifiant
def update(id, updatedTask):
    data = load_data()
    
    for task in data['tasks']:
        if task['id'] == id:
            task['task'] = updatedTask
    
    save_data(data)

#supprime une tâche, retrouvée grâce à son identifiant
#On crée une liste avec toutes les tâches sauf celles avec l'identifiant choisi
def delete(id):
    data = load_data()
    initial_count = len(data['tasks'])
    
    data['tasks'] = [task for task in data['tasks'] if task['id'] != id]
    if len(data['tasks']) < initial_count:
        save_data(data)
        print(f"Tâche {id} supprimée.")
    else:
        print(f"Aucune tâche trouvée avec l'id {id}")
 
#Mise à jour du niveau de progression, on récupère l'identifiant et le niveau de progression souhaité
def updateProgress(id, progress):
    data = load_data()
    
    if progress not in ['Todo', 'In Progress', 'Done']:
        print("Only accepted values : 'Todo', 'In Progress', 'Done'")
    
    for task in data['tasks']:
        if task['id'] == id:
            task['progression'] = progress
    
    save_data(data)

#On liste les différentes tâches par status
def listByStatus():
    data = load_data()
    status = ['Todo', 'In Progress', 'Done']
    
    for st in status:
        print('')
        print(f'Progression - {st}')
        for task in data['tasks']:
            if task['progression'] == st:
                print(f"{task['id']} - {task['task']}")

#Gestion des commandes grâce à argparse
def main():
    
    parser = argparse.ArgumentParser(description="Gérer une liste de tâches")
    subparsers = parser.add_subparsers(dest="command", help="Sous-commandes")
    
    # Commande "Add"
    parser_add = subparsers.add_parser("add", help="Ajouter une tâche")
    parser_add.add_argument("task", type=str, help="La tâche à ajouter")

    # Commande "List"
    subparsers.add_parser("list", help="Lister les tâches")

    # Commande "Update"
    parser_update = subparsers.add_parser("update", help="Met à jour une tâche")
    parser_update.add_argument("id", type=int, help="Identifiant de la tâche")
    parser_update.add_argument("newtask", type=str, help="Nouveau texte pour la tâche")

    # Commande "Delete"
    parser_delete = subparsers.add_parser('delete', help="Supprimer une tâche")
    parser_delete.add_argument('id', type=int, help="Identifiant de la tâche")

    # Commande "UpdateProgress"
    parser_update_progress = subparsers.add_parser('updateprogress', help="Modifie le niveau de progression")
    parser_update_progress.add_argument('id', type=int, help="Identifiant de la tâche")
    parser_update_progress.add_argument('progress', type=str, help="Nouveau stage de progression : Todo, In Progress, Done")
    
    # Commande "ListByStatus"
    subparsers.add_parser('liststatus', help="Liste par status")

    args = parser.parse_args()
    
    if args.command == "add":
        add(args.task)
    if args.command == "list":
        list()
    if args.command == "update":
        update(args.id, args.newtask)
    if args.command == "delete":
        delete(args.id)
    if args.command == "updateprogress":
        updateProgress(args.id, args.progress)
    if args.command == "liststatus":
        listByStatus()

if __name__ == "__main__":
    main()
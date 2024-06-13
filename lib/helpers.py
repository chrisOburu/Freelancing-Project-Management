from models.client import Client
from models.freelancer import Freelancer
from models.project import Project
from prettytable.colortable import ColorTable, Themes

table = ColorTable(theme=Themes.OCEAN)

# Project functions
def list_projects():
    table.clear()
    projects = Project.get_all()
    projects_list = [(project.id,project.name, project.client_id, project.freelancer_id) for project in projects]
    headers = ["ID","Tittle", "Client ID", "Freelancer ID"]
    table.field_names= headers
    for i in projects_list:
        table.add_row(i)

    print(table)

def find_project_by_name():
    table.clear()
    name = input("Enter the project's name: ")
    project = Project.find_by_name(name)
    if project:
        project_list = [(project.id, project.name, project.client_id, project.freelancer_id)]
        headers = ["ID", "Name", "Client ID", "Freelancer ID"]
        table.field_names= headers
        for i in project_list:
            table.add_row(i)
        print(table)
    
    else:
        print(f'Project {name} not found')
   

def find_project_by_id():
    table.clear()
    id_ = input("Enter the project's id: ")
    project = Project.find_by_id(id_)
    if project:
        project_list = [(project.id, project.name, project.client_id, project.freelancer_id)]
        headers = ["ID", "Name", "Client ID", "Freelancer ID"]
        table.field_names= headers
        for i in project_list:
            table.add_row(i)
        print(table)
    
    else:
        print(f'Project {id_} not found')
    

def create_project():
    table.clear()
    name = input("Enter the project's name: ")
    freelancer_id = input("Enter the freelancer's id: ")
    client_id = input("Enter the client's id: ")
    try:
        project = Project.create(name, freelancer_id, client_id)
        print(f'Successfuly created project')
        project_list = [(project.id, project.name, project.client_id, project.freelancer_id)]
        headers = ["ID", "Name", "Client ID", "Freelancer ID"]
        table.field_names= headers
        for i in project_list:
            table.add_row(i)
        print(table)
    except Exception as exc:
        print("Error creating project: ", exc)

def update_project():
    table.clear()
    id_ = input("Enter the project's id: ")
    if project := Project.find_by_id(id_):
        try:
            name = input("Enter the project's new name: ")
            project.name = name
            freelancer_id = input("Enter the freelancer's id: ")
            project.freelancer_id = freelancer_id
            client_id = input("Enter the client's id: ")
            project.client_id = client_id

            project.update()
            print(f'Successfully updated project')
            project_list = [(project.id, project.name, project.client_id, project.freelancer_id)]
            headers = ["ID", "Name", "Client ID", "Freelancer ID"]
            table.field_names= headers
            for i in project_list:
                table.add_row(i)
            print(table)
        except Exception as exc:
            print("Error updating project: ", exc)
    else:
        print(f'Project {id_} not found')

def delete_project():
    id_ = input("Enter the project's id: ")
    if project := Project.find_by_id(id_):
        project.delete()
        print(f'Project {id_} deleted')
    else:
        print(f'Project {id_} not found')

def list_clients():
    table.clear()
    clients = Client.get_all()
    client_list = [(client.client_id, client.name, client.username) for client in clients]
    headers = ["ID", "Name", "Username"]
    table.field_names= headers
    for i in client_list:
        table.add_row(i)

    print(table)

def find_client_by_name():
    table.clear()
    name = input("Enter the client's name: ")
    client = Client.find_by_name(name)
    if client:
        client_list = [(client.client_id, client.name, client.username)]
        headers = ["ID", "Name", "Username"]
        table.field_names= headers
        for i in client_list:
            table.add_row(i)
        print(table)
    
    else:
        print(f'Client {name} not found')

def find_client_by_id():
    table.clear()
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    if client:
        client_list = [(client.client_id, client.name, client.username)]
        headers = ["ID", "Name", "Username"]
        table.field_names= headers
        for i in client_list:
            table.add_row(i)
        print(table)
    
    else:
        print(f'Client {id_} not found')

def create_client():
    table.clear()
    name = input("Enter the client's name: ")
    username = input("Enter the client's username: ")
    try:
        client = Client.create(name, username)
        print(f'Successfuly created client')
        client_list = [(client.client_id, client.name, client.username)]
        headers = ["ID", "Name", "Username"]
        table.field_names= headers
        for i in client_list:
            table.add_row(i)
        print(table)
    except Exception as exc:
        print("Error creating client: ", exc)

def update_client():
    table.clear()
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        try:
            name = input("Enter the client's new name: ")
            client.name = name
            username = input("Enter the client's new username: ")
            client.username = username

            client.update()
            print(f'Successfully updated client')
            client_list = [(client.client_id, client.name, client.username)]
            headers = ["ID", "Name", "Username"]
            table.field_names= headers
            for i in client_list:
                table.add_row(i)
            print(table)
        except Exception as exc:
            print("Error updating client: ", exc)
    else:
        print(f'Client {id_} not found')

def delete_client():
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        client.delete()
        print(f'Client {id_} deleted')
    else:
        print(f'Client {id_} not found')

def list_freelancers():
    table.clear()
    freelancers = Freelancer.get_all()
    freelancer_list = [(freelancer.freelancer_id, freelancer.name, freelancer.username) for freelancer in freelancers]
    headers = ["ID", "Name", "Username"]
    table.field_names= headers
    for i in freelancer_list:
        table.add_row(i)

    print(table)

def find_freelancer_by_name():
    table.clear()
    name = input("Enter the freelancer's name: ")
    freelancer = Freelancer.find_by_name(name)
    if freelancer:
        freelancer_list = [(freelancer.freelancer_id, freelancer.name, freelancer.username)]
        headers = ["ID", "Name", "Username"]
        table.field_names= headers
        for i in freelancer_list:
            table.add_row(i)
        print(table)
    
    else:
        print(f'Freelancer {name} not found')

def find_freelancer_by_id():
    table.clear()
    id_ = input("Enter the freelancer's id: ")
    freelancer = Freelancer.find_by_id(id_)
    if freelancer:
        freelancer_list = [(freelancer.freelancer_id, freelancer.name, freelancer.username)]
        headers = ["ID", "Name", "Username"]
        table.field_names= headers
        for i in freelancer_list:
            table.add_row(i)
        print(table)
    
    else:
        print(f'Freelancer {id_} not found')

def create_freelancer():
    table.clear()
    name = input("Enter the freelancer's name: ")
    username = input("Enter the freelancer's username: ")
    try:
        freelancer = Freelancer.create(name, username)
        print(f'Successfuly created freelancer')
        freelancer_list = [(freelancer.freelancer_id, freelancer.name, freelancer.username)]
        headers = ["ID", "Name", "Username"]
        table.field_names= headers
        for i in freelancer_list:
            table.add_row(i)
        print(table)
    except Exception as exc:
        print("Error creating freelancer: ", exc)

def update_freelancer():
    table.clear()
    id_ = input("Enter the freelancer's id: ")
    if freelancer := Freelancer.find_by_id(id_):
        try:
            name = input("Enter the freelancer's new name: ")
            freelancer.name = name
            username = input("Enter the freelancer's new username: ")
            freelancer.username = username

            freelancer.update()
            print(f'Successfully updated freelancer')
            freelancer_list = [(freelancer.freelancer_id, freelancer.name, freelancer.username)]
            headers = ["ID", "Name", "Username"]
            table.field_names= headers
            for i in freelancer_list:
                table.add_row(i)
            print(table)
        except Exception as exc:
            print("Error updating freelancer: ", exc)
    else:
        print(f'Freelancer {id_} not found')

def delete_freelancer():
    id_ = input("Enter the freelancer's id: ")
    if freelancer := Freelancer.find_by_id(id_):
        freelancer.delete()
        print(f'Freelancer {id_} deleted')
    else:
        print(f'Freelancer {id_} not found')
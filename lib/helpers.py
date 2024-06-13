from models.client import Client
from models.freelancer import Freelancer
from models.project import Project


# Project functions

def list_projects():
    projects = Project.get_all()
    for project in projects:
        print(project)


def find_project_by_name():
    name = input("Enter the project's name: ")
    project = Project.find_by_name(name)
    print(project) if project else print(
        f'Project {name} not found')


def find_project_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the project's id: ")
    project = Project.find_by_id(id_)
    print(project) if project else print(f'Project {id_} not found')


def create_project():
    name = input("Enter the project's name: ")
    freelancer_id = input("Enter the freelancer's id: ")
    client_id = input("Enter the client's id: ")
    try:
        project = Project.create(name, freelancer_id,client_id)
        print(f'Success: {project}')
    except Exception as exc:
        print("Error creating project: ", exc)


def update_project():
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
            print(f'Success: {project}')
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
    clients = Client.get_all()
    for client in clients:
        print(client)


def find_client_by_name():
    name = input("Enter the client's name: ")
    client = Client.find_by_name(name)
    print(client) if client else print(
        f'Client {name} not found')


def find_client_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    print(client) if client else print(f'Client {id_} not found')


def create_client():
    name = input("Enter the client's name: ")
    username = input("Enter the client's username: ")
    try:
        client = Client.create(name, username)
        print(f'Success: {client}')
    except Exception as exc:
        print("Error creating client: ", exc)


def update_client():
    id_ = input("Enter the client's id: ")
    if client := Client.find_by_id(id_):
        try:
            name = input("Enter the client's new name: ")
            client.name = name
            username = input("Enter the client's new username: ")
            client.username = username

            client.update()
            print(f'Success: {client}')
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


# You'll implement the employee functions in the lab

def list_freelancers():
    freelancers = Freelancer.get_all()
    for freelancer in freelancers:
        print(freelancer)


def find_freelancer_by_name():
    name = input("Enter the freelancer's name: ")
    freelancer = Freelancer.find_by_name(name)
    print(freelancer) if freelancer else print(
        f'Freelancer {name} not found')


def find_freelancer_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the freelancer's id: ")
    freelancer = Freelancer.find_by_id(id_)
    print(freelancer) if freelancer else print(f'Freelancer {id_} not found')


def create_freelancer():
    name = input("Enter the freelancer's name: ")
    username = input("Enter the freelancer's username: ")
    try:
        freelancer = Freelancer.create(name, username)
        print(f'Success: {freelancer}')
    except Exception as exc:
        print("Error creating freelancer: ", exc)


def update_freelancer():
    id_ = input("Enter the freelancer's id: ")
    if freelancer := Freelancer.find_by_id(id_):
        try:
            name = input("Enter the freelancer's new name: ")
            freelancer.name = name
            username = input("Enter the freelancer's new username: ")
            freelancer.username = username

            freelancer.update()
            print(f'Success: {freelancer}')
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
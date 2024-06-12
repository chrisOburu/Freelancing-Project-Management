from models.client import Client
from models.freelancer import Freelancer
from models.project import Project


def exit_program():
    print("Goodbye!")
    exit()

# Client functions

def list_clients():
    clients = Client.get_all()
    for client in clients:
        print(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}, Address: {client.address}")

def find_client_by_name():
    name = input("Enter the client's name: ")
    client = Client.find_by_name(name)
    if client:
        print(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}, Address: {client.address}")
    else:
        print(f'Client {name} not found')

def find_client_by_id():
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    if client:
        print(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}, Address: {client.address}")
    else:
        print(f'Client {id_} not found')

def create_client():
    name = input("Enter the client's name: ")
    email = input("Enter the client's email: ")
    phone = input("Enter the client's phone: ")
    address = input("Enter the client's address: ")

    try:
        client = Client.create(name, email, phone, address)
        print(f'Success: ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}, Address: {client.address}')
    except Exception as exc:
        print('Error creating client: ', exc)

def update_client():
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    if client:
        try:
            name = input(f"Enter the client's new name (leave blank to keep current: {client.name}): ")
            email = input(f"Enter the client's new email (leave blank to keep current: {client.email}): ")
            phone = input(f"Enter the client's new phone (leave blank to keep current: {client.phone}): ")
            address = input(f"Enter the client's new address (leave blank to keep current: {client.address}): ")

            if name:
                client.name = name
            if email:
                client.email = email
            if phone:
                client.phone = phone
            if address:
                client.address = address

            client.update()
            print(f'Success: ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}, Address: {client.address}')
        except Exception as exc:
            print("Error updating client: ", exc)
    else:
        print(f'Client {id_} not found')

def delete_client():
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    if client:
        try:
            client.delete()
            print(f'Client {id_} deleted')
        except Exception as exc:
            print("Error deleting client: ", exc)
    else:
        print(f'Client {id_} not found')

def list_client_freelancers():
    id_ = input("Enter the client's id: ")
    client = Client.find_by_id(id_)
    if client:
        freelancers = client.list_freelancers()
        for freelancer in freelancers:
            print(f"ID: {freelancer.freelancer_id}, Username: {freelancer.username}, Email: {freelancer.email}, Name: {freelancer.name}")
    else:
        print(f'Client {id_} not found')

# Freelancer functions

def list_freelancers():
    freelancers = Freelancer.list_freelancers()
    for freelancer in freelancers:
        print(f"ID: {freelancer.freelancer_id}, Username: {freelancer.username}, Email: {freelancer.email}, Name: {freelancer.name}")

def find_freelancer_by_name():
    name = input("Enter the freelancer's name: ")
    freelancer = Freelancer.find_freelancer_by_name(name)
    if freelancer:
        print(f"ID: {freelancer.freelancer_id}, Username: {freelancer.username}, Email: {freelancer.email}, Name: {freelancer.name}")
    else:
        print(f'Freelancer {name} not found')

def find_freelancer_by_id():
    id_ = input("Enter the freelancer's id: ")
    freelancer = Freelancer.find_freelancer_by_id(id_)
    if freelancer:
        print(f"ID: {freelancer.freelancer_id}, Username: {freelancer.username}, Email: {freelancer.email}, Name: {freelancer.name}")
    else:
        print(f'Freelancer {id_} not found')

def create_freelancer():
    freelancer_id = input("Enter the freelancer's id: ")
    username = input("Enter the freelancer's username: ")
    email = input("Enter the freelancer's email: ")
    name = input("Enter the freelancer's name: ")

    try:
        freelancer = Freelancer.create_freelancer(freelancer_id, username, email, name)
        print(f'Success: ID: {freelancer.freelancer_id}, Username: {freelancer.username}, Email: {freelancer.email}, Name: {freelancer.name}')
    except Exception as exc:
        print('Error creating freelancer: ', exc)

def update_freelancer():
    id_ = input("Enter the freelancer's id: ")
    freelancer = Freelancer.find_freelancer_by_id(id_)
    if freelancer:
        try:
            username = input(f"Enter the freelancer's new username (leave blank to keep current: {freelancer.username}): ")
            email = input(f"Enter the freelancer's new email (leave blank to keep current: {freelancer.email}): ")
            name = input(f"Enter the freelancer's new name (leave blank to keep current: {freelancer.name}): ")

            freelancer.update_freelancer(
                username=username if username else None,
                email=email if email else None,
                name=name if name else None
            )
            print(f'Success: ID: {freelancer.freelancer_id}, Username: {freelancer.username}, Email: {freelancer.email}, Name: {freelancer.name}')
        except Exception as exc:
            print("Error updating freelancer: ", exc)
    else:
        print(f'Freelancer {id_} not found')

def delete_freelancer():
    id_ = input("Enter the freelancer's id: ")
    freelancer = Freelancer.find_freelancer_by_id(id_)
    if freelancer:
        try:
            freelancer.delete_freelancer()
            print(f'Freelancer {id_} deleted')
        except Exception as exc:
            print("Error deleting freelancer: ", exc)
    else:
        print(f'Freelancer {id_} not found')

def list_freelancer_clients():
    id_ = input("Enter the freelancer's id: ")
    freelancer = Freelancer.find_freelancer_by_id(id_)
    if freelancer:
        clients = freelancer.list_freelancer_clients()
        for client in clients:
            print(f"ID: {client.id}, Name: {client.name}, Email: {client.email}")
    else:
        print(f'Freelancer {id_} not found')

# Project functions

def list_projects():
    pass

def find_project_by_name():
    pass

def find_project_by_id():
    pass

def create_project():
    pass

def update_project():
    pass

def delete_project():
    pass

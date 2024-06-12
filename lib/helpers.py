from models.client import Client
from models.freelancer import FreelancerManager
from models.project import Project

freelancer_manager = FreelancerManager()

def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the client functions in this lesson

def list_clients():
    pass

def find_client_by_name():
    pass

def find_client_by_id():
    pass

def create_client():
    pass

def update_client():
    pass

def delete_client():
    pass

def list_client_freelancers():
    pass


# Implement the freelancer functions

def list_freelancers():
    freelancers = freelancer_manager.list_freelancers()
    for freelancer in freelancers:
        print(freelancer)

def find_freelancer_by_name():
    name = input("Enter the freelancer's name: ")
    freelancer = freelancer_manager.find_freelancer_by_name(name)
    print(freelancer) if freelancer else print(f'Freelancer {name} not found')

def find_freelancer_by_id():
    id_ = input("Enter the freelancer's id: ")
    freelancer = freelancer_manager.find_freelancer_by_id(id_)
    print(freelancer) if freelancer else print(f'Freelancer {id_} not found')

def create_freelancer():
    freelancer_id = input("Enter the freelancer's id: ")
    username = input("Enter the freelancer's username: ")
    email = input("Enter the freelancer's email: ")
    password = input("Enter the freelancer's password: ")
    name = input("Enter the freelancer's name: ")
    surname = input("Enter the freelancer's surname: ")

    try:
        freelancer = freelancer_manager.create_freelancer(freelancer_id, username, email, password, name, surname)
        print(f'Success: {freelancer}')
    except Exception as exc:
        print('Error creating freelancer: ', exc)

def update_freelancer():
    id_ = input("Enter the freelancer's id: ")
    if freelancer := freelancer_manager.find_freelancer_by_id(id_):
        try:
            name = input("Enter the freelancer's new name (leave blank to keep current): ")
            skills = input("Enter the freelancer's new skills (comma separated, leave blank to keep current): ")
            hourly_rate = input("Enter the freelancer's new hourly rate (leave blank to keep current): ")
            
            skills = skills.split(",") if skills else None
            hourly_rate = float(hourly_rate) if hourly_rate else None
            
            freelancer = freelancer_manager.update_freelancer(id_, name, skills, hourly_rate)
            print(f'Success: {freelancer}')
        except Exception as exc:
            print("Error updating freelancer: ", exc)
    else:
        print(f'Freelancer {id_} not found')

def delete_freelancer():
    id_ = input("Enter the freelancer's id: ")
    if freelancer := freelancer_manager.find_freelancer_by_id(id_):
        try:
            freelancer_manager.delete_freelancer(id_)
            print(f'Freelancer {id_} deleted')
        except Exception as exc:
            print("Error deleting freelancer: ", exc)
    else:
        print(f'Freelancer {id_} not found')

def list_freelancer_clients():
    id_ = input("Enter the freelancer's id: ")
    if freelancer := freelancer_manager.find_freelancer_by_id(id_):
        clients = freelancer_manager.list_freelancer_clients(id_)
        for client in clients:
            print(client)
    else:
        print(f'Freelancer {id_} not found')


# You'll implement the project functions

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
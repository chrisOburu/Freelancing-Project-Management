# from pyfiglet import figlet_format
# from colorama import init, Fore
# import random
# import os

# init()

# lg = Fore.LIGHTGREEN_EX
# w = Fore.WHITE
# cy = Fore.CYAN
# ye = Fore.YELLOW
# rs = Fore.RESET
# r = Fore.RED
# n = Fore.RESET
# colors = [lg, r, cy, ye]
# plus = lg + '(' + w + '+' + lg + ')' + rs


# def banner():
#     banner = figlet_format('FPM',font="roman",width=400)
#     print(f'{r}{banner}{n}')


# def clr():
#     if os.name == 'nt':
#         os.system('cls')
#     else:
#         os.system('clear')

# def exit_program():
#     print("Goodbye!")
#     clr()
#     exit()
   


# from helpers import (
#     # CLIENT
#     list_clients,
#     find_client_by_name,
#     find_client_by_id,
#     create_client,
#     update_client,
#     delete_client,
#     #list_client_freelancers,


#     # FREELANCER
#     list_freelancers,
#     find_freelancer_by_name,
#     find_freelancer_by_id,
#     create_freelancer,
#     update_freelancer,
#     delete_freelancer,
#     #list__freelancer_clients,

#     # PROJECT
#     list_projects,
#     find_project_by_name,
#     find_project_by_id,
#     create_project,
#     update_project,
#     delete_project,
# )


# def main():
#     while True:
#         clr()
#         banner()
#         table_menu()
#         table_choice = input("> ")
#         if table_choice == "0":
#             exit_program()
#         elif table_choice == "1":
#             while True:
#                 # clr()
#                 # banner()
#                 project_menu()
#                 project_choice = input("> ")
#                 if project_choice == "0":
#                     break
#                 handle_project_choice(project_choice)
#         elif table_choice == "2":
#             while True:
#                 # clr()
#                 # banner()
#                 client_menu()
#                 client_choice = input("> ")
#                 if client_choice == "0":
#                     break
#                 handle_client_choice(client_choice)
#         elif table_choice == "3":
#             while True:
#                 # clr()
#                 # banner()
#                 freelancer_menu()
#                 freelancer_choice = input("> ")
#                 if freelancer_choice == "0":
#                     break
#                 handle_freelancer_choice(freelancer_choice)
        
#         else:
#             print("Invalid choice")


# def table_menu():
#     print("Please select a table to interact with:")
#     print("0. Exit the program")
#     print("1. Project Table")
#     print("2. Client Table")
#     print("3. Freelancer Table")
    


# def client_menu():
#     print("Client Menu:")
#     print("0. Back to main menu")
#     print("1. List all clients")
#     print("2. Find client by name")
#     print("3. Find client by id")
#     print("4. Create client")
#     print("5. Update client")
#     print("6. Delete client")
#     print("7. List all freelancers of a client")


# def freelancer_menu():
#     print("Freelancer Menu:")
#     print("0. Back to main menu")
#     print("1. List all freelancers")
#     print("2. Find freelancer by name")
#     print("3. Find freelancer by id")
#     print("4. Create freelancer")
#     print("5. Update freelancer")
#     print("6. Delete freelancer")
#     print("7. List all clients of a freelancer")


# def project_menu():
#     print("Project Menu:")
#     print("0. Back to main menu")
#     print("1. List all projects")
#     print("2. Find project by name")
#     print("3. Find project by id")
#     print("4. Create project")
#     print("5. Update project")
#     print("6. Delete project")


# def handle_client_choice(choice):
#     if choice == "0":
#         return False
#     elif choice == "1":
#         list_clients()
#     elif choice == "2":
#         find_client_by_name()
#     elif choice == "3":
#         find_client_by_id()
#     elif choice == "4":
#         create_client()
#     elif choice == "5":
#         update_client()
#     elif choice == "6":
#         delete_client()
#     elif choice == "6":
#         delete_client()
#     elif choice == "7":
#         pass
#         #list_client_freelancers()
#     else:
#         print("Invalid choice")


# def handle_freelancer_choice(choice):
#     if choice == "0":
#         return False
#     elif choice == "1":
#         list_freelancers()
#     elif choice == "2":
#         find_freelancer_by_name()
#     elif choice == "3":
#         find_freelancer_by_id()
#     elif choice == "4":
#         create_freelancer()
#     elif choice == "5":
#         update_freelancer()
#     elif choice == "6":
#         delete_freelancer()
#     elif choice == "7":
#         pass
#         #list__freelancer_clients()
#     else:
#         print("Invalid choice")


# def handle_project_choice(choice):
#     if choice == "0":
#         return False
#     elif choice == "1":
#         list_projects()
#     elif choice == "2":
#         find_project_by_name()
#     elif choice == "3":
#         find_project_by_id()
#     elif choice == "4":
#         create_project()
#     elif choice == "5":
#         update_project()
#     elif choice == "6":
#         delete_project()
#     else:
#         print("Invalid choice")


# if __name__ == "__main__":
#     main()


from pyfiglet import figlet_format
from colorama import init, Fore
import os

init()

# Define color variables
lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
rs = Fore.RESET
r = Fore.RED
n = Fore.RESET
colors = [lg, r, cy, ye]

def banner():
    print(f'{r}{figlet_format("FPM", font="roman", width=400)}{n}')

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    print("Goodbye!")
    clr()
    exit()

from helpers import (
    list_clients,
    find_client_by_name,
    find_client_by_id,
    create_client,
    update_client,
    delete_client,
    list_freelancers,
    find_freelancer_by_name,
    find_freelancer_by_id,
    create_freelancer,
    update_freelancer,
    delete_freelancer,
    list_projects,
    find_project_by_name,
    find_project_by_id,
    create_project,
    update_project,
    delete_project,
)

def main():
    while True:
        clr()
        banner()
        table_menu()
        table_choice = input("> ")
        if table_choice == "0":
            exit_program()
        elif table_choice == "1":
            while True:
                project_menu()
                project_choice = input("> ")
                if project_choice == "0":
                    break
                handle_project_choice(project_choice)
        elif table_choice == "2":
            while True:
                client_menu()
                client_choice = input("> ")
                if client_choice == "0":
                    break
                handle_client_choice(client_choice)
        elif table_choice == "3":
            while True:
                freelancer_menu()
                freelancer_choice = input("> ")
                if freelancer_choice == "0":
                    break
                handle_freelancer_choice(freelancer_choice)
        else:
            print("Invalid choice")

def table_menu():
    print(f"{w}Please select a table to interact with:")
    print(f"{lg}0. Exit the program")
    print("1. Project Table")
    print("2. Client Table")
    print("3. Freelancer Table")
    print(n)

def client_menu():
    print(f"{w}Client Menu:")
    print(f"{lg}0. Back to main menu")
    print("1. List all clients")
    print("2. Find client by name")
    print("3. Find client by id")
    print("4. Create client")
    print("5. Update client")
    print("6. Delete client")
    print(n)

def freelancer_menu():
    print(f"{w}Freelancer Menu:")
    print(f"{lg}0. Back to main menu")
    print("1. List all freelancers")
    print("2. Find freelancer by name")
    print("3. Find freelancer by id")
    print("4. Create freelancer")
    print("5. Update freelancer")
    print("6. Delete freelancer")
    print(n)

def project_menu():
    print(f"{w}Project Menu:")
    print(f"{lg}0. Back to main menu")
    print("1. List all projects")
    print("2. Find project by name")
    print("3. Find project by id")
    print("4. Create project")
    print("5. Update project")
    print("6. Delete project")
    print(n)

def handle_client_choice(choice):
    if choice == "1":
        list_clients()
    elif choice == "2":
        find_client_by_name()
    elif choice == "3":
        find_client_by_id()
    elif choice == "4":
        create_client()
    elif choice == "5":
        update_client()
    elif choice == "6":
        delete_client()
    else:
        print("Invalid choice")

def handle_freelancer_choice(choice):
    if choice == "1":
        list_freelancers()
    elif choice == "2":
        find_freelancer_by_name()
    elif choice == "3":
        find_freelancer_by_id()
    elif choice == "4":
        create_freelancer()
    elif choice == "5":
        update_freelancer()
    elif choice == "6":
        delete_freelancer()
    else:
        print("Invalid choice")

def handle_project_choice(choice):
    if choice == "1":
        list_projects()
    elif choice == "2":
        find_project_by_name()
    elif choice == "3":
        find_project_by_id()
    elif choice == "4":
        create_project()
    elif choice == "5":
        update_project()
    elif choice == "6":
        delete_project()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

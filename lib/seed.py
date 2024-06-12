#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.client import Client
from models.freelancer import Freelancer
from models.project import Project

def seed_database():
    Freelancer.drop_table()
    Client.drop_table()
    Client.create_table()
    Freelancer.create_table()

    # Create seed data
    payroll = client.create("Payroll", "Building A, 5th Floor")
    human_resources = client.create(
        "Human Resources", "Building C, East Wing")
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", human_resources.id)
    Employee.create("Dani", "Benefits Coordinator", human_resources.id)
    Employee.create("Hao", "New Hires Coordinator", human_resources.id)


seed_database()
print("Seeded database")

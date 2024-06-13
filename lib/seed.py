#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.client import Client
from models.freelancer import Freelancer
from models.project import Project
from faker import Faker
import random
import string

def generate_username(length=8):
    letters = string.ascii_lowercase
    digits = string.digits
    all_characters = letters + digits
    username = ''.join(random.choice(all_characters) for _ in range(length))
    return username

def generate_random_gig_title():
    adjectives = ['Professional', 'Experienced', 'Creative', 'Expert', 'Skilled', 'Talented']
    services = ['Writer', 'Graphic Designer', 'Web Developer', 'SEO Specialist', 'Social Media Manager', 'Data Analyst']
    specifics = ['for Blogs', 'for Websites', 'for E-commerce', 'for Small Businesses', 'for Startups', 'for Social Media']

    adjective = random.choice(adjectives)
    service = random.choice(services)
    specific = random.choice(specifics)

    return f"{adjective} {service} {specific}"

def seed_database():
    Freelancer.drop_table()
    Client.drop_table()
    Client.create_table()
    Freelancer.create_table()
    Project.drop_table()
    Project.create_table()

    # Create seed data
    clients = []
    freelancers = []

    for i in range(10):
        fake = Faker()
        client = Client.create(generate_username(),fake.name())
        clients.append(client)
        freelancer = Freelancer.create(generate_username(),fake.name())
        freelancers.append(freelancer)

    for i in range(20):
        fake = Faker()
        Project.create(generate_random_gig_title(), random.choice(freelancers).freelancer_id, random.choice(clients).client_id)

    

seed_database()
print("Seeded database")

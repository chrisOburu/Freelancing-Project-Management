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
    Project.drop_table()
    Project.create_table()

    # Create seed data
    cl1=Client.create("JJGJG","UJGM958")
    cl2=Client.create("OBOB","YRFJF98")
    fr1=Freelancer.create("ggjjj","tghyhhhnhn")
    fr2=Freelancer.create("OBOttyyuuB","yyynjuj667")

    Project.create("HGJFKF",fr2.freelancer_id,cl1.client_id)
    Project.create("wjcdcknjc",fr1.freelancer_id,cl2.client_id)


    

seed_database()
print("Seeded database")

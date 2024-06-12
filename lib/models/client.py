from models.__init__ import CURSOR, CONN

class Client:
    def __init__(self, id, name, email, phone, address):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

        
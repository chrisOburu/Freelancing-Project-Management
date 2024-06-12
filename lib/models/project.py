from models.__init__ import CURSOR, CONN
from freelancer import Freelancer
from client import Client

class Project:
    all = []

    def __init__(self, freelancer, client):
        if not isinstance(freelancer, Freelancer):
            raise ValueError("Freelancer must be an instance of Freelancer")
        if not isinstance(client, Client):
            raise ValueError("Client must be an instance of Client")
        self._client = client
        self._freelancer = freelancer
        Project.all.append(self)

    @property
    def client(self):
        return self._client

    @property
    def freelancer(self):
        return self._freelancer

    @freelancer.setter
    def freelancer(self, value):
        if not isinstance(value, Freelancer):
            raise ValueError("freelancer must be an instance of freelancer")
        self._freelancer = value

    @client.setter
    def client(self, value):
        if not isinstance(value, Client):
            raise ValueError("client must be an instance of client")
        self._client = value
        
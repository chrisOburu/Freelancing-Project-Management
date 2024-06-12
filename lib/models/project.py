from models.__init__ import CURSOR, CONN

class Project:
    def __init__(self, id, name, description, created_at, updated_at):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.tasks = []
        self.users = []
        self.comments = []
        self.files = []
        self.labels = []
        self.status = None
        self.due_date = None
        self.priority = None

        
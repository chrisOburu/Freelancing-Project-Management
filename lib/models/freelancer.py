from models.__init__ import CURSOR, CONN

class Freelancer:
    def __init__(self, freelancer_id, username, email, password, name, surname):
        self.freelancer_id = freelancer_id
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.skills = []
        self.projects = []
        self.ratings = []
        self.earnings = 0
        self.balance = 0
        self.is_active = True
        self.is_admin = False
        self.is_blocked = False
        self.is_deleted = False
        self.created_at = None
        self.updated_at = None

        
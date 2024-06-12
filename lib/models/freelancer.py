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

    def save_to_database(self):
        sql = """
        INSERT INTO freelancers (freelancer_id, username, email, password, name, surname, 
        is_active, is_admin, is_blocked, is_deleted, created_at, updated_at) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.freelancer_id, self.username, self.email, self.password, self.name, self.surname, 
                             self.is_active, self.is_admin, self.is_blocked, self.is_deleted, self.created_at, self.updated_at))
        CONN.commit()

    @classmethod
    def load_from_database(cls, freelancer_id):
        sql = "SELECT * FROM freelancers WHERE freelancer_id = ?"
        CURSOR.execute(sql, (freelancer_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

class FreelancerManager:
    def __init__(self):
        self.freelancers = []

    def list_freelancers(self):
        return self.freelancers

    def find_freelancer_by_id(self, freelancer_id):
        for freelancer in self.freelancers:
            if freelancer.freelancer_id == freelancer_id:
                return freelancer
        return None

    def find_freelancer_by_name(self, freelancer_name):
        for freelancer in self.freelancers:
            if freelancer.name == freelancer_name:
                return freelancer
        return None

    def create_freelancer(self, freelancer_id, username, email, password, name, surname):
        if self.find_freelancer_by_id(freelancer_id):
            raise ValueError("Freelancer with this ID already exists.")
        freelancer = Freelancer(freelancer_id, username, email, password, name, surname)
        freelancer.save_to_database()
        self.freelancers.append(freelancer)
        return freelancer

    def update_freelancer(self, freelancer_id, name=None, skills=None, hourly_rate=None):
        freelancer = self.find_freelancer_by_id(freelancer_id)
        if freelancer:
            if name:
                freelancer.name = name
            if skills:
                freelancer.skills = skills
            if hourly_rate:
                freelancer.hourly_rate = hourly_rate
            sql = "UPDATE freelancers SET name = ?, skills = ?, hourly_rate = ? WHERE freelancer_id = ?"
            CURSOR.execute(sql, (freelancer.name, freelancer.skills, freelancer.hourly_rate, freelancer.freelancer_id))
            CONN.commit()
            return freelancer
        raise ValueError("Freelancer with this ID does not exist.")

    def delete_freelancer(self, freelancer_id):
        freelancer = self.find_freelancer_by_id(freelancer_id)
        if freelancer:
            self.freelancers.remove(freelancer)
            sql = "DELETE FROM freelancers WHERE freelancer_id = ?"
            CURSOR.execute(sql, (freelancer_id,))
            CONN.commit()
            return True
        return False

    def list_freelancer_clients(self, freelancer_id):
        freelancer = self.find_freelancer_by_id(freelancer_id)
        if freelancer:
            return freelancer.clients
        return None

        

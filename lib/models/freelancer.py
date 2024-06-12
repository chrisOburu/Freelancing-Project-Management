from models.__init__ import CURSOR, CONN

class Freelancer:
    def __init__(self, freelancer_id, username, email, name):
        self.freelancer_id = freelancer_id
        self.username = username
        self.email = email
        self.name = name
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
        self.clients = []  # List of client IDs

    def save_to_database(self):
        """Save the freelancer to the database."""
        sql = """
        INSERT INTO freelancers (freelancer_id, username, email, name, 
        is_active, is_admin, is_blocked, is_deleted, created_at, updated_at) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.freelancer_id, self.username, self.email, self.name, 
                             self.is_active, self.is_admin, self.is_blocked, self.is_deleted, self.created_at, self.updated_at))
        CONN.commit()

    @classmethod
    def load_from_database(cls, freelancer_id):
        """Load a freelancer from the database by ID."""
        sql = "SELECT * FROM freelancers WHERE freelancer_id = ?"
        CURSOR.execute(sql, (freelancer_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def list_freelancers(cls):
        """List all registered freelancers."""
        sql = "SELECT * FROM freelancers"
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        freelancers = [cls(*row) for row in rows]
        return freelancers

    @classmethod
    def find_freelancer_by_id(cls, freelancer_id):
        """Find a freelancer by ID."""
        sql = "SELECT * FROM freelancers WHERE freelancer_id = ?"
        CURSOR.execute(sql, (freelancer_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def find_freelancer_by_name(cls, freelancer_name):
        """Find a freelancer by name."""
        sql = "SELECT * FROM freelancers WHERE name = ?"
        CURSOR.execute(sql, (freelancer_name,))
        row = CURSOR.fetchone()
        if row:
            return cls(*row)
        return None

    @classmethod
    def create_freelancer(cls, freelancer_id, username, email, name):
        """Create a new freelancer."""
        if cls.find_freelancer_by_id(freelancer_id):
            raise ValueError("Freelancer with this ID already exists.")
        freelancer = cls(freelancer_id, username, email, name)
        freelancer.save_to_database()
        return freelancer

    def update_freelancer(self, username=None, email=None, name=None):
        """Update freelancer's information."""
        if username:
            self.username = username
        if email:
            self.email = email
        if name:
            self.name = name
        self.save_to_database()

    def delete_freelancer(self):
        """Delete the freelancer."""
        self.is_deleted = True
        self.save_to_database()

    def list_freelancer_clients(self):
        """List clients of the freelancer."""
        clients = []
        for client_id in self.clients:
            client = Client.find_client_by_id(client_id)
            if client:
                clients.append(client)
        return clients



        

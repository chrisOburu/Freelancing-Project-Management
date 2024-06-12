# from models.__init__ import CURSOR, CONN
# from models.client import Client

# class Freelancer:
#     def _init_(self, freelancer_id, username, email, name):
#         self.freelancer_id = freelancer_id
#         self.username = username
#         self.email = email
#         self.name = name
#         self.projects = []
#         self.clients = []  # List of client IDs

#     def save_to_database(self):
#         """Save the freelancer to the database."""
#         sql = """
#         INSERT INTO freelancers (freelancer_id, username, email, name, 
#         is_active, is_admin, is_blocked, is_deleted, created_at, updated_at) 
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """
#         CURSOR.execute(sql, (self.freelancer_id, self.username, self.email, self.name))
#         CONN.commit()

#     @classmethod
#     def load_from_database(cls, freelancer_id):
#         """Load a freelancer from the database by ID."""
#         sql = "SELECT * FROM freelancers WHERE freelancer_id = ?"
#         CURSOR.execute(sql, (freelancer_id,))
#         row = CURSOR.fetchone()
#         if row:
#             return cls(*row)
#         return None

#     @classmethod
#     def list_freelancers(cls):
#         """List all registered freelancers."""
#         sql = "SELECT * FROM freelancers"
#         CURSOR.execute(sql)
#         rows = CURSOR.fetchall()
#         freelancers = [cls(*row) for row in rows]
#         return freelancers

#     @classmethod
#     def find_freelancer_by_id(cls, freelancer_id):
#         """Find a freelancer by ID."""
#         sql = "SELECT * FROM freelancers WHERE freelancer_id = ?"
#         CURSOR.execute(sql, (freelancer_id,))
#         row = CURSOR.fetchone()
#         if row:
#             return cls(*row)
#         return None

#     @classmethod
#     def find_freelancer_by_name(cls, freelancer_name):
#         """Find a freelancer by name."""
#         sql = "SELECT * FROM freelancers WHERE name = ?"
#         CURSOR.execute(sql, (freelancer_name,))
#         row = CURSOR.fetchone()
#         if row:
#             return cls(*row)
#         return None

#     @classmethod
#     def create_freelancer(cls, freelancer_id, username, email, name):
#         """Create a new freelancer."""
#         if cls.find_freelancer_by_id(freelancer_id):
#             raise ValueError("Freelancer with this ID already exists.")
#         freelancer = cls(freelancer_id, username, email, name)
#         freelancer.save_to_database()
#         return freelancer

#     def update_freelancer(self, username=None, email=None, name=None):
#         """Update freelancer's information."""
#         if username:
#             self.username = username
#         if email:
#             self.email = email
#         if name:
#             self.name = name
#         self.save_to_database()

#     def delete_freelancer(self):
#         """Delete the freelancer."""
#         self.is_deleted = True
#         self.save_to_database()

#     def list_freelancer_clients(self):
#         """List clients of the freelancer."""
#         clients = []
#         for client_id in self.clients:
#             client = Client.find_client_by_id(client_id)
#             if client:
#                 clients.append(client)
#         return clients


# lib/models/department.py
from models.__init__ import CURSOR, CONN


class Department:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError(
                "Location must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Department instances """
        sql = """
            DROP TABLE IF EXISTS departments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Department instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO departments (name, location)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        """ Initialize a new Department instance and save the object to the database """
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        """Update the table row corresponding to the current Department instance."""
        sql = """
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Department instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM departments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Department object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        department = cls.all.get(row[0])
        if department:
            # ensure attributes match row values in case local instance was modified
            department.name = row[1]
            department.location = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            department = cls(row[1], row[2])
            department.id = row[0]
            cls.all[department.id] = department
        return department

    @classmethod
    def get_all(cls):
        """Return a list containing a Department object per row in the table"""
        sql = """
            SELECT *
            FROM departments
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Department object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM departments
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Department object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM departments
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def employees(self):
        """Return list of employees associated with current department"""
        from models.employee import Employee
        sql = """
            SELECT * FROM employees
            WHERE department_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Employee.instance_from_db(row) for row in rows
        ]


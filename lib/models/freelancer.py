# from models.__init__ import CURSOR, CONN
# from models.freelancer import Freelancer

# class Freelancer:
#     def _init_(self, freelancer_id, username, email, name):
#         self.freelancer_id = freelancer_id
#         self.username = username
#         self.email = email
#         self.name = name
#         self.projects = []
#         self.freelancers = []  # List of freelancer IDs

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

#     def list_freelancer_freelancers(self):
#         """List freelancers of the freelancer."""
#         freelancers = []
#         for freelancer_id in self.freelancers:
#             freelancer = Freelancer.find_freelancer_by_id(freelancer_id)
#             if freelancer:
#                 freelancers.append(freelancer)
#         return freelancers


# lib/models/department.py

from models.__init__ import CURSOR, CONN


class Freelancer:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, username, name,freelancer_id=None):
        self.freelancer_id = freelancer_id
        self.name = name
        self.username = username

    def __repr__(self):
        return f"<Freelancer {self.freelancer_id}: {self.name}, {self.username}>"

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
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username):
            self._username = username
        else:
            raise ValueError(
                "Location must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Freelancer instances """
        sql = """
            CREATE TABLE IF NOT EXISTS freelancers (
            freelancer_id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Freelancer instances """
        sql = """
            DROP TABLE IF EXISTS freelancers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and username values of the current Freelancer instance.
        Update object freelancer_id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO freelancers (name, username)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.username))
        CONN.commit()

        self.freelancer_id = CURSOR.lastrowid
        type(self).all[self.freelancer_id] = self

    @classmethod
    def create(cls, name, username):
        """ Initialize a new Freelancer instance and save the object to the database """
        freelancer = cls(name, username)
        freelancer.save()
        return freelancer

    def update(self):
        """Update the table row corresponding to the current Freelancer instance."""
        sql = """
            UPDATE freelancers
            SET name = ?, username = ?
            WHERE freelancer_id = ?
        """
        CURSOR.execute(sql, (self.name, self.username, self.freelancer_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Freelancer instance,
        delete the dictionary entry, and reassign freelancer_id attribute"""

        sql = """
            DELETE FROM freelancers
            WHERE freelancer_id = ?
        """

        CURSOR.execute(sql, (self.freelancer_id,))
        CONN.commit()

        # Delete the dictionary entry using freelancer_id as the key
        del type(self).all[self.freelancer_id]

        # Set the freelancer_id to None
        self.freelancer_id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Freelancer object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        freelancer = cls.all.get(row[0])
        if freelancer:
            # ensure attributes match row values in case local instance was modified
            freelancer.name = row[1]
            freelancer.username = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            freelancer = cls(row[1], row[2])
            freelancer.freelancer_id = row[0]
            cls.all[freelancer.freelancer_id] = freelancer
        return freelancer

    @classmethod
    def get_all(cls):
        """Return a list containing a Freelancer object per row in the table"""
        sql = """
            SELECT *
            FROM freelancers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, freelancer_id):
        """Return a Freelancer object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM freelancers
            WHERE freelancer_id = ?
        """

        row = CURSOR.execute(sql, (freelancer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Freelancer object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM freelancers
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    #TODO check
    def employees(self):
        """Return list of employees associated with current freelancer"""
        from models.project import Project
        sql = """
            SELECT * FROM employees
            WHERE freelancer_freelancer_id = ?
        """
        CURSOR.execute(sql, (self.freelancer_id,),)

        rows = CURSOR.fetchall()
        return [
            Project.instance_from_db(row) for row in rows
        ]


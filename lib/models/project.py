# lib/models/project.py
from models.__init__ import CURSOR, CONN
from models.client import Client
from models.freelancer import Freelancer


class Project:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, client_id,freelancer_id, id=None):
        self.id = id
        self.name = name
        self.client_id = client_id
        self.freelancer_id = freelancer_id

    def __repr__(self):
        return f"<Project {self.id}: {self.name}, Client ID: {self.client_id}>"+ f"Freelancer ID: {self.freelancer_id}>"
        

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
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        client_id = int(client_id)
        if type(client_id) is int and Client.find_by_id(client_id):
            self._client_id = client_id
        else:
            raise ValueError(
                "client_id must reference a client in the database")
    @property
    def freelancer_id(self):
        return self._freelancer_id

    @freelancer_id.setter
    def freelancer_id(self, freelancer_id):
        freelancer_id = int(freelancer_id)
        if type(freelancer_id) is int and Freelancer.find_by_id(freelancer_id):
            self._freelancer_id = freelancer_id
        else:
            raise ValueError(
                "client_id must reference a client in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Project instances """
        sql = """
            CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT,
            freelancer_id TEXT,
            client_id INTEGER,
            FOREIGN KEY (client_id) REFERENCES clients(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Project instances """
        sql = """
            DROP TABLE IF EXISTS projects;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, job title, and client id values of the current Project object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO projects (name, freelancer_id, client_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.freelancer_id,self.client_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Project instance."""
        sql = """
            UPDATE projects
            SET name = ?, freelancer_id = ?, client_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.freelancer_id,
                             self.client_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Project instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM projects
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, freelancer_id, client_id):
        """ Initialize a new Project instance and save the object to the database """
        project = cls(name, freelancer_id, client_id)
        project.save()
        return project

    @classmethod
    def instance_from_db(cls, row):
        """Return an Project object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        project = cls.all.get(row[0])
        if project:
            # ensure attributes match row values in case local instance was modified
            project.name = row[1]
            project.freelancer_id = row[2]
            project.client_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            project = cls(row[1], row[2], row[3])
            project.id = row[0]
            cls.all[project.id] = project
        return project

    @classmethod
    def get_all(cls):
        """Return a list containing one Project object per table row"""
        sql = """
            SELECT *
            FROM projects
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        id = int(id)
        """Return Project object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM projects
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Project object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM projects
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

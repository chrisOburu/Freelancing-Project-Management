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


# from models.__init__ import CURSOR, CONN


# class Client:

#     all = {} # objects saved to database

#     def __init__(self, name, email, phone, address, client_id = None):
#         self.client_id = client_id
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.address = address
        

#     def __repr__(self):
#             return (
#                 f"<Client {self.client_id}: {self.name}, {self.email},  {self.phone}, {self.address}>"
#             )

#     @property
#     def name(self):
#         return self._name


#     @name.setter
#     def name(self, name):
#         if isinstance(name, str) and len(name):
#             self._name = name
#         else:
#             raise ValueError(
#                 "Name must be a non-empty string"
#             )
            
#     @property
#     def email(self):
#         return self._email


#     @email.setter
#     def email(self, email):
#         if isinstance(email, str) and len(email):
#             self._email = email
#         else:
#             raise ValueError(
#                 "Email must be a non empty string"
#             )
        
#     @property
#     def phone(self):
#         return self._phone

#     @phone.setter
#     def phone(self, phone):
#         if isinstance(phone, str) and len(phone):
#                 self._phone = phone
#         else:
#             raise ValueError(
#                 "Phone number must be a non-empty string"
#             )
        

#     @property
#     def address(self):
#         return self._address


#     @address.setter
#     def address(self, address):
#         if isinstance(address, str) and len(address):
#             self.address = address
#         else:
#             raise ValueError(
#                 "Address cannot be empty"
#             )
        
#     @classmethod
#     def create_table(cls):
#         """ Create a new table to persist the attributes of Client instances """
#         sql = """
#         CREATE TABLE IF NOT EXISTS clients (
#         client_id INTEGER PRIMARY KEY,
#             name TEXT,
#             email TEXT,
#             phone TEXT,
#             address TEXT)
#         """
#         CURSOR.execute(sql)
#         CONN.commit()


#     @classmethod
#     def drop_table(cls):
#         """ Drop the table that persists Client instances """
#         sql = """
#             DROP TABLE IF EXISTS clients;
#         """
#         CURSOR.execute(sql)
#         CONN.commit()


#     def save(self):
#         """ Insert a new row with the name, email, phone and address values of the current Client object.
#         Update object client_id attribute using the primary key value of new row.
#         Save the object in local dictionary using table row's PK as dictionary key"""
#         sql = """
#                 INSERT INTO clients (name, email, phone, address)
#                 VALUES (?, ?, ?)
#         """

#         CURSOR.execute(sql,(self.name, self.email, self.phone, self.address))
#         CONN.commit()

#         self.client_id = CURSOR.lastrowclient_id
#         type(self).all[self.client_id] = self


#     def update(self):
#         """Update the table row corresponding to the current Client instance."""
#         sql = """
#             UPDATE clients
#             SET name = ?, email = ?, address = ?, phone = ?, address = ?
#             WHERE client_id = ?
#         """
#         CURSOR.execute(sql, (self.name, self.email, self.phone, self.address, self.client_id))
#         CONN.commit()


#     def delete(self):
#         """Delete the table row corresponding to the current Client instance,
#         delete the dictionary entry, and reassign client_id attribute"""

#         sql = """
#             DELETE FROM clients
#             WHERE client_id = ?
#         """

#         CURSOR.execute(sql, (self.client_id,))
#         CONN.commit()

#         # Delete the dictionary entry using client_id as the key
#         del type(self).all[self.client_id]

#         # Set the client_id to None
#         self.client_id = None


#     @classmethod
#     def create(cls, name, email, phone, address):
#         """ Initialize a new Client instance and save the object to the database """
#         client = cls(name, email, phone, address)
#         client.save()
#         return client


#     @classmethod
#     def instance_from_db(cls, row):
#         """Return a Client object having the attribute values from the table row."""

#         # Check the dictionary for existing instance using the row's primary key
#         client = cls.all.get(row[0])
#         if client:
#             # ensure attributes match row values in case local instance was modified
#             client.name = row[1]
#             client.email = row[2]
#             client.phone = row[3]
#             client.address = row[4]
#         else:
#             # not in dictionary, create new instance and add to dictionary
#             client = cls(row[1], row[2], row[3], row[4])
#             client.client_id = row[0]
#             cls.all[client.client_id] = client
#         return client


#     @classmethod
#     def get_all(cls):
#         """Return a list containing one Client object per table row"""
#         sql = """
#             SELECT *
#             FROM clients
#         """

#         rows = CURSOR.execute(sql).fetchall()

#         return [cls.instance_from_db(row) for row in rows]


#     @classmethod
#     def find_by_client_id(cls, client_id):
#         """Return Client object corresponding to the table row matching the specified primary key"""
#         sql = """
#             SELECT *
#             FROM clients
#             WHERE client_id = ?
#         """

#         row = CURSOR.execute(sql, (client_id,)).fetchone()
#         return cls.instance_from_db(row) if row else None


#     @classmethod
#     def find_by_name(cls, name):
#         """Return Client object corresponding to first table row matching specified name"""
#         sql = """
#             SELECT *
#             FROM clients
#             WHERE name = ?
#         """

#         row = CURSOR.execute(sql, (name,)).fetchone()
#         return cls.instance_from_db(row) if row else None


# lib/models/client.py
from models.__init__ import CURSOR, CONN


class Client:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, client_id, username, name):
        self.client_id = client_id
        self.name = name
        self.username = username

    def __repr__(self):
        return f"<Client {self.client_id}: {self.name}, {self.username}>"

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
        """ Create a new table to persist the attributes of Client instances """
        sql = """
            CREATE TABLE IF NOT EXISTS clients (
            client_id INTEGER PRIMARY KEY,
            name TEXT,
            username TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Client instances """
        sql = """
            DROP TABLE IF EXISTS clients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and username values of the current Client instance.
        Update object client_id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO clients (name, username)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.username))
        CONN.commit()

        self.client_id = CURSOR.lastrowclient_id
        type(self).all[self.client_id] = self

    @classmethod
    def create(cls, name, username):
        """ Initialize a new Client instance and save the object to the database """
        client = cls(name, username)
        client.save()
        return client

    def update(self):
        """Update the table row corresponding to the current Client instance."""
        sql = """
            UPDATE clients
            SET name = ?, username = ?
            WHERE client_id = ?
        """
        CURSOR.execute(sql, (self.name, self.username, self.client_id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Client instance,
        delete the dictionary entry, and reassign client_id attribute"""

        sql = """
            DELETE FROM clients
            WHERE client_id = ?
        """

        CURSOR.execute(sql, (self.client_id,))
        CONN.commit()

        # Delete the dictionary entry using client_id as the key
        del type(self).all[self.client_id]

        # Set the client_id to None
        self.client_id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Client object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        client = cls.all.get(row[0])
        if client:
            # ensure attributes match row values in case local instance was modified
            client.name = row[1]
            client.username = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            client = cls(row[1], row[2])
            client.client_id = row[0]
            cls.all[client.client_id] = client
        return client

    @classmethod
    def get_all(cls):
        """Return a list containing a Client object per row in the table"""
        sql = """
            SELECT *
            FROM clients
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_client_id(cls, client_id):
        """Return a Client object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM clients
            WHERE client_id = ?
        """

        row = CURSOR.execute(sql, (client_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Client object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM clients
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    #TODO check
    def employees(self):
        """Return list of employees associated with current client"""
        from models.project import Project
        sql = """
            SELECT * FROM employees
            WHERE client_client_id = ?
        """
        CURSOR.execute(sql, (self.client_id,),)

        rows = CURSOR.fetchall()
        return [
            Project.instance_from_db(row) for row in rows
        ]


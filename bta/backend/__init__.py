# This file is part of the BTA toolset
# (c) EADS CERT and EADS Innovation Works


class Backend(object):
    backends={}
    @classmethod
    def register(cls, name):
        def doreg(c):
            cls.backends[name.lower()] = c
            return c
        return doreg
    @classmethod
    def get_backend(cls, name):
        return cls.backends[name.lower()]

    def __init__(self, options, connection=None):
        self.options = options
        self.connection = connection if connection is not None else options.connection

    def commit(self):
        pass

    def create_table(self):
        raise NotImplementedError("Backend.create_table()")
    def open_table(self):
        raise NotImplementedError("Backend.open_table()")
    def list_tables(self):
        raise NotImplementedError("Backend.list_tables()")



class BackendTable(object):
    def __init__(self, options, db, name):
        self.options = options
        self.db = db
        self.name = name

    def create(self):
        raise NotImplementedError("Table.create()")

    def create_with_fields(self, columns):
        raise NotImplementedError("Table.create_with_fields()")
    def insert_fields(self, values):
        raise NotImplementedError("Table.insert_fields()")
    def create_index(self, colname):
        raise NotImplementedError("Table.create_index()")

    def count(self):
        raise NotImplementedError("Table.count()")
    def find(self, *args, **kargs):
        raise NotImplementedError("Table.find()")
    def find_one(self, *args, **kargs):
        raise NotImplementedError("Table.find_one()")

    def insert(self, values):
        raise NotImplementedError("Table.insert()")
    def update(self, *args):
        raise NotImplementedError("Table.update()")



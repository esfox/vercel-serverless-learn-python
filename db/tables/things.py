from estoult import *
from db.connection import connection

class Thing(connection.Schema):
    __tablename__ = 'things'
    id = Field(int)
    name = Field(str)

class Things:
    def get_all(self):
        return (
            Query(Thing)
            .select()
            .execute()
        )

    def create(self, thing):
        return Thing.insert(thing)

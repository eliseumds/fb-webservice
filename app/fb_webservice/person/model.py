from fb_webservice.db import BaseMainModel
from peewee import *

__all__ = ['Person']

class Person(BaseMainModel):
    id = TextField(primary_key=True)
    name = TextField()
    gender = TextField()
    username = TextField()

Person.create_table(True)

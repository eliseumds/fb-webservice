import datetime
from fb_webservice.db import BaseLogModel
from peewee import *

__all__ = ['Log']

class Log(BaseLogModel):
    arguments = TextField(null=True)
    date = DateTimeField(default=datetime.datetime.now)
    text = TextField()
    type = TextField()

Log.create_table(True)

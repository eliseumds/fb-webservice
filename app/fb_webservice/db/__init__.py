from tornado.options import options
from peewee import create_model_tables,Model,SqliteDatabase
from tornado.options import options

__all__ = ['BaseLogModel','BaseMainModel']

DBLog = SqliteDatabase(options.db_main)
DBLog.connect()

DBMain = SqliteDatabase(options.db_log)
DBMain.connect()

class BaseLogModel(Model):
    class Meta:
        database = DBLog

class BaseMainModel(Model):
    class Meta:
        database = DBMain

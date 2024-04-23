from peewee import *

class DefaultModel(Model):
    class Meta:
        database = SqliteDatabase('ZPROJECT/ZDB.db')

class Users(DefaultModel):
    username = CharField(max_length=32, unique=True, index=True)
    password = CharField(max_length=32)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64, null=True)
    bio = TextField(null=True)
    isadmin = BooleanField()

class Posts(DefaultModel):
    author = ForeignKeyField(Users, backref='posts', on_delete='CASCADE')
    text = TextField()
    time = DateTimeField()
    like = IntegerField()


DefaultModel._meta.database.connect()
DefaultModel._meta.database.create_tables([Users, Posts])


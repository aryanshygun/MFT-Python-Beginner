from peewee import *
import json
import os
db = SqliteDatabase('Edu/MFT-Python/Final Project/Z_project.db')

class DefaultModel(Model):
    class Meta:
        database = db

class Users(DefaultModel):
    username = CharField(max_length=32, unique=True, index=True)
    password = CharField(max_length=32)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64, null=True)
    bio = TextField(null=True)
    isadmin = BooleanField()

class Posts(DefaultModel):
    author = CharField()
    text = TextField()
    time = DateTimeField()
    like = IntegerField()

# db.connect()
# db.create_tables([Users, Posts])

class Actions:
    @staticmethod
    def add_tables():
        # db.connect()
        db.create_tables([Users,Posts])
    
    @staticmethod
    def add():
        user_path = 'Edu/MFT-Python/Final Project/users.json'
        with open(user_path, 'r') as file:
            users = json.load(file)
        for username, user_info in users.items():
            exists = Users.select().where(Users.username == username)
            if exists.exists():
                pass
            else:
                Users.create(
                    username=username,
                    password=user_info['password'],
                    first_name=user_info['first_name'],
                    last_name=user_info['last_name'],
                    bio=user_info['bio'],
                    isadmin=user_info['isadmin']
                )
            
        post_path = 'Edu/MFT-Python/Final Project/posts.json'
        with open(post_path, 'r') as file:
            posts = json.load(file)
            
        for post_id, post_info in posts.items():
            Posts.create(
                post_id=post_id,
                author=post_info['author'],
                text=post_info['text'],
                time=post_info['time'],
                like=post_info['like']
            )
    
    @staticmethod
    def drop_tables():
        for i in db.get_indexes():
            i.drop_table()
    
    @staticmethod
    # def update_db():
    #     user_path = 'Edu/MFT-Python/Final Project/users.json'
    #     with open(user_path, 'r') as file:
    #         users = json.load(file)
            
    #         for username, user_info in users.items():
    #             if username not in 
        
            
        
            
def execute_database():
    if not os.path.exists('Edu/MFT-Python/Final Project/Z_project.db'):
        db.connect()
        Actions.add_tables()
        Actions.add()

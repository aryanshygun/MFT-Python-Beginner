from modelmigrate import Users, Posts
import json


__user_path = 'ZPROJECT/users_list.json'

with open(__user_path, 'r') as f:
    users = json.load(f)


for i in users:
    query = Users.select().where(Users.username == i)
    if not query.exists():
        Users.create(
            username=i,
            password=users[i]['password'],
            first_name=users[i]['name']['first_name'],
            last_name=users[i]['name']['last_name'],
            bio=users[i]['bio'],
            isadmin=users[i]['isadmin'],
        )

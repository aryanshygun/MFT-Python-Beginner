from modelmigrate import Users, Posts
import json


__post_path = 'ZPROJECT/posts_list.json'



with open(__post_path, 'r') as file:
    posts = json.load(file)

for i in posts:
    Posts.create(
        author=Users.select().where(Users.username == posts[i]['author']).get(),
        text=posts[i]['text'],
        time=posts[i]['time'],
        like=posts[i]['like']
    )
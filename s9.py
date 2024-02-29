import json
from datetime import datetime
import time 
__user_path = 'MFT-Python/user.json'
__post_path = 'MFT-Python/post.json'

with open(__user_path, 'r') as f:
    users = json.load(f)
with open(__post_path, 'r') as f:
    posts = json.load(f)
    

def register_user():
    User_username = input('username: ')
    User_password = input('password: ')
    User_fname = input("first name: ")
    User_lname = input("last name")
    User_bio = input('bio: ')
    User_admin = input('is admin: ')
    User_admin = True if User_admin == 'YES' else False
    users[User_username] = {
        'password': User_password,
        'name': {
            'first_name': User_fname,
            'last_name': User_lname,
        },
        'bio': User_bio,
        'admin': User_admin
    }
    with open(__user_path, 'w') as f:
        json.dump(users, f, indent=4)

def show_users():
    for i,j in users.items():
        print('/\\/\\/\\/\\/\\/\\/\\/\\/')
        user_show =[
            f"{i} - {j['name']['first_name']} {j['name']['last_name']}",
            f"bio: {j['bio']}",
            f"is admin: {j['admin']}"]
        print('\n'.join(user_show))


def add_post(username):
    post_num = len(posts) + 1
    # post_author =  users.keys()
    post_text = input('text: ')
    
    posts[post_num] = {
        "author": username,
        "text": post_text,
        "time": f'{time.time()}',
        "like": '0',
    }
    with open(__post_path, 'w') as f:
        json.dump(posts, f, indent=4)

def show_post():
    for i in posts.values():
        print('/\\/\\/\\/\\/\\/\\/\\/\\/')
        t = datetime.fromtimestamp(int(float(i['time']))).strftime('%Y-%m-%d %H:%M')
        post_show=[
            f"{i['author']}",
            f"{i['text']}",
            f"{t} - {i['like']}"
        ]
        print('\n'.join(post_show))

    



def banner(username, admin=False):
    s = ['----------------------------', 'be Y khosh amadid',
         '1.', '2. add post', '3. show post', '4. show users', '5. logout', '0. exit']
    if admin:
        s.insert(7, "6. register user")
    s = '\n'.join(s)
    # menu_input = None
    # while menu_input != '0':
    
    while True:
        print(s)
        menu_input = input('enter your input: ')
        if menu_input == '1':
            pass
        elif menu_input == '2':
            add_post(username)
        elif menu_input == '3':
            show_post()
        elif menu_input == '4':
            show_users()
        elif menu_input == '5':
            return 0
        elif menu_input == '6' and admin:
            register_user()
        elif menu_input == '0':
            return -1

def login():
    username = input('username : ')
    password = input('password : ')
    if (u := users.get(username)) is not None:
        if u['password'] == password:
            print('login success')
            stat = banner(username , u['admin'])
            if stat == 0:
                return
            elif stat == -1:
                exit()
        else:
            print('invalid usename or password')
    else:
        print('invalid usename or password')

while True:
    login()
    print('loging out')
    
    
    

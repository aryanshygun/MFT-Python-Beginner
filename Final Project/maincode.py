import time
from modelmigrate import *
import json
import os
from adminpass import secretpassword
import subprocess

class SocialMedia:

    def __init__(self) -> None:
        self.active_user = None
        self.__users_path = 'ZPROJECT/users_list.json'
        self.__posts_path = 'ZPROJECT/posts_list.json'
        print("--------------------------------------------------")
        
    def login(self):
        
        if not os.path.exists(self.__users_path):
            print('No users found')
            print('Initializing the Users-list')
            with open(self.__users_path, 'w') as file:
                json.dump({}, file, indent=4)
                print('Initializing the Super-admin')
            admin_check = input('Are you an admin? Y/N\n')
            while True:
                
                if admin_check == 'N':
                    print('So long padner...')
                    return False
                elif admin_check == 'Y':
                    password_check = input('Enter the maximum security password:\n')
                    while True:
                        if password_check == secretpassword:
                            print("Congrats son, You're now the Super-Admin")
                            self.register_user(admin= True)
                            # break
                        else:
                            print("Mission failed, You'll get 'em next time ")
                else:
                    print('Invalid answer. Git Gud')
                    
        else:        
            print("--------------------------------------------------")
            user_name = input('Enter your username:\n')
            pass_word = input('Enter your password:\n')
            user_check = Users.select().where(Users.username == user_name)
            while True:
                if user_check.exists():
                    currect_user = user_check.get()
                    if currect_user.password == pass_word:
                        print('Successful login')
                        self.active_user = currect_user
                        self.banner()
                        break
                    else:
                        print('Invalid username or password')
                else:
                    print('Invalid username or password')
    
    def register_user(self, admin= False):
        User_username = input('username:\n')
        if Users.select().where(Users.username == User_username).exists():
            print('this username already exists.')
            return False
        
        if admin == True:
            pass
        else:
            while True:
                sub_admin_check = input('Is this person yet another admin? Y/N:\n')
                if sub_admin_check == 'Y':
                    admin = True
                    break
                elif sub_admin_check == 'N':
                    admin = False
                    break
                else:
                    print('invalid answer, try again')


        with open(self.__users_path, 'r') as file:
            userlist = json.load(file)
        userlist[User_username] = {
            "password": input('password:\n'),
            "name": {
                "first_name": input("first name:\n"),
                "last_name": input('last name:\n')
            },
            "bio": input('bio:\n'),
            "isadmin": admin}

        with open(self.__users_path, 'w') as file:
            json.dump(userlist, file, indent=4)
            
        subprocess.run(['python3', 'ZPROJECT/usertodb.py'], bufsize=0)
        print('user created successfully')
        self.active_user = Users.select().where(Users.username == User_username).get()
        self.banner()
        return True
    
    def show_users(self):
        for i in Users.select():
            print("--------------------------------------------------")
            user_show = [
                f'{i.username} - {i.first_name} {i.last_name}',
                f'bio: {i.bio}'
            ]
            print('\n\n'.join(user_show))
            print("--------------------------------------------------")
    
    def add_post(self):
        
        if not os.path.exists(self.__posts_path):
            with open(self.__posts_path, 'w') as file2:
                json.dump({}, file2, indent=4)
        
        text = input('enter your text:\n')
        with open(self.__posts_path, 'r') as file:
            postlist = json.load(file)
        postlist[len(postlist) + 1] = {
            'author': self.active_user.username,
            'text': text,
            'time': time.ctime(),
            'like': 0
        }

        with open(self.__posts_path, 'w') as file:
            json.dump(postlist, file, indent=4) 
        subprocess.run(['python3', 'ZPROJECT/posttodb.py'], bufsize=0)
        print('user created successfully')
    
    def show_posts(self):
        for i in Posts.select():
            print("--------------------------------------------------")
            post_show = [
                f'user: {i.author.username}',
                f'text: {i.text}',
                f'time: {i.time}',
                f'like: {i.like}'
            ]
            print('\n\n'.join(post_show))
            print("--------------------------------------------------")
    def banner(self):
        s = f'''
        -=-=-=-=-=-=-=-=-=-=-=-=-
        welcome to Z, {self.active_user.username}!
        0. Exit
        1. Add Post
        2. Show Posts
        3. Show Users
        4. Logout
        '''
        if self.active_user.isadmin:
            s += '''5. Register User
            '''
        while True:
            print("--------------------------------------------------")
            # print(f'current user: {self.active_user.username}')
            print(s)
            inp = input('enter your input: ')
            if inp == '1':
                self.add_post()
            elif inp == '2':
                self.show_posts()
            elif inp == '3':
                self.show_users()
            elif inp == '4':
                self.active_user = None
                print('logging out')
                app.login()
                return
            elif inp == '0':
                print('bye!')
                print("--------------------------------------------------")
                exit()
            elif inp == '5' and self.active_user.isadmin:
                self.register_user()

   
app = SocialMedia()

def main():
    app.login()

if __name__ == '__main__':
    main()
from modules import *
class SocialMedia:
    
    __users_path = 'Edu/MFT-Python/Final Project/users.json'
    __posts_path = 'Edu/MFT-Python/Final Project/posts.json'
    
    def __init__(self) -> None:
        self.active_user = None
        execute_database()
        
    ############################################    
    # LOADING - DUMPING
    ############################################  
    
    def load_users(self):
        with open(self.__users_path, 'r') as file:
            return json.load(file)
    
    def dump_users(self,x):
        with open(self.__users_path, 'w') as file:
            json.dump(x, file, indent=4)
        
    def load_posts(self):
        with open(self.__posts_path, 'r') as file:
            return json.load(file)
        
    def dump_posts(self,x):
        with open(self.__posts_path, 'w') as file:
            json.dump(x, file, indent=4)
            
    ############################################    
    # HEADER - LOGIN - REGISTRATION - TERMINATION - EXITTING
    ############################################ 
       
    def header(self):
        print("\\\\//   \\\\//   \\\\//   \\\\//   \\\\//   \\\\//   \\\\//")
        print("   \\\\//   \\\\//   \\\\//   \\\\//   \\\\//   \\\\//   ")
        print("\\\\//   \\\\//   \\\\//   \\\\//   \\\\//   \\\\//   \\\\//") 
        
    def login(self):
        self.header()
        print('Hi! please enter your username!')
        while True:
            username = input()
            if Users.select().where(Users.username == username).exists():
                self.active_user = Users.select().where(Users.username == username).get()
                print(f'Hi {self.active_user.first_name} {self.active_user.last_name}!\nplease enter your password:')
                while True:
                    active_user_password = input()
                    if active_user_password == self.active_user.password:
                        print('Congrats! You are now logged in.')
                        self.banner()
                        break
                    print('Incorrect password, Try again!') 
            print('Unfortunately this username is not registered yet! Try again\n')
        
    # def registration(self):
    #     print("Enter the person's username:")
    #     while True:
    #         username = input()
    #         if Users.select().where(Users.username == username).exists():
    #             print('Unfortunately this username already exists, Try again!\n')
    #         break
    #     print("Would this person be another admin? Y/N")      
    #     while True:
    #         isadmin = input()
    #         if isadmin == "Y":
    #             isadmin = True
    #             break
    #         elif isadmin == "N":
    #             isadmin = False
    #             break
    #         else:
    #             print("Invalid Response, Try again!\n")
    #     userlist = self.load_users()
    #     userlist[username] = {
    #         "first_name": username.title(),
    #         "last_name": input('Enter their last name:\n').title(),
    #         "password": input('Enter their password:\n'),
    #         "bio": input('bio:\n'),
    #         "isadmin": isadmin}
    #     self.dump_users(userlist)
    #     os.remove('Edu/MFT-Python/Final Project/Z_project.db')
    #     Actions.add_tables()
    #     Actions.add()
    #     print('User added to database successfully.')
        # return True
    
    # def termination(self, status): 
    #     self.view_list(status)
    #     print("--------------------------------------------------")
    #     id = int(input("Enter the person's ID\n"))
    #     terminate = status.get(status.id == id)
    #     if terminate.isadmin == True:
    #         print('You cant terminate another admin.\n')
    #         return True
    #     terminate.delete_instance()
    #     print('User terminated.\n')
    #     print("--------------------------------------------------")
    #     return True
    
    # def exitting(self):
    #     print('Bye!')
    #     self.header()
    #     self.login()
         
    ############################################    
    # VIEWING - POSTING
    ############################################  
    def view_list(self, status):
        if status == Users:
            for i in Users.select():
                print("--------------------------------------------------")
                user_show = [
                    f'{i.id}',
                    f'{i.username} - {i.first_name} {i.last_name}',
                    f'Bio: {i.bio}',
                    f'Admin Status: {i.isadmin}'
                ]
                print('\n'.join(user_show))
                print("--------------------------------------------------")
        elif status == Posts:
            for i in Posts.select():
                print("--------------------------------------------------")
                post_show = [
                    f'{i}',
                    f'Author: {i.author}',
                    f'Text: {i.text}',
                    f'Time: {i.time}',
                    f'Like: {i.like}'
                ]
                print('\n'.join(post_show))
                print("--------------------------------------------------")
                
    def add_post(self):
        postlist = self.load_posts()
        postlist[len(postlist) + 1] = {
            'author': self.active_user.username,
            'text': input('Type your post:\n'),
            'time': time.ctime(),
            'like': 0 }
        self.dump_posts(postlist)
        print('user created successfully')

    ############################################    
    # BANNER
    ############################################          
    def banner(self):
        self.header()
        if self.active_user.isadmin == True:
            banner = [
                '-=-=-=-=-=-=-=-=-=-=-=-=-',
                f'Welcome to the Z Social media, Admin {self.active_user.first_name}!',
                '',
                '1. View - Users ',
                '2. View - Posts ',
                '',
                '3. Register  - Users',
                '4. Terminate - Users',
                '',
                '5. Exit',
                '-=-=-=-=-=-=-=-=-=-=-=-=-',
                '']  
            print('Navigate by entering the respective number:')
            while True:
                print('\n'.join(banner))
                inp = int(input())
                if inp == 1:
                    self.view_list(Users)
                elif inp == 2:
                    self.view_list(Posts)
                elif inp == 3:
                    self.registration()
                elif inp == 4:
                    self.termination()
                elif inp == 5:
                    self.exitting()
        elif self.active_user.isadmin == False:
            banner = [
                '-=-=-=-=-=-=-=-=-=-=-=-=-',
                f'Welcome to the Z Social media, User {self.active_user.first_name}!',
                '',
                '1. View - Users ',
                '2. View - Posts ',
                '',
                '3. Exit',
                '-=-=-=-=-=-=-=-=-=-=-=-=-',
                '']  
            print('Navigate by entering the respective number:')
            while True:
                print('\n'.join(banner))
                inp = int(input())
                if inp == 1:
                    self.view_list(Users)
                elif inp == 2:
                    self.view_list(Posts)
                elif inp == 3:
                    self.exitting()

app = SocialMedia()
if __name__ == '__main__':
    app.login()

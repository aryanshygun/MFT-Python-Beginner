from model import *

class Hospital:
    
    def __init__(self):
        self.active_staff = None
    
    def login(self):
        print("Hello, please enter your username:")
        while True:
            username = input()
            if not Staff.select().where(Staff.username == username).exists():
                print("Invalid username, try again!")
            else:
                self.active_staff = Staff.get(Staff.username == username)
                print(f"Hi {self.active_staff.first_name} {self.active_staff.last_name}! Please enter your password:")
                while True:
                    password = int(input())
                    if not self.active_staff.password == password:
                        print("Invalid password, Try again!")
                    else:
                        print("Congrats! You're now logged in.")
                        self.banner()
                        break
            
    def registeration(self,status):
        if status == Patients:
            status.create(
                national_id = int(input("Enter the patient's national ID:\n")),
                first_name = input("Enter their first name:\n"),
                last_name = input("Enter their last name:\n"),
                age = int(input("Enter their age:\n")),
                refered_doctor = self.set_refered(Doctors),
                status = True)
        elif status == Doctors:
            status.create(
                work_code = int(input("Enter the doctor's work code:\n")),
                first_name = input("Enter their first name:\n"),
                last_name = input("Enter their last name:\n"),
                department = input("Enter their department:\n"),
                status = True)
        elif status == Surgeryrooms:
            status.create(
                name = input("Enter it's name:\n"),
                refered_patient = self.set_refered(Patients),
                refered_doctor = self.set_refered(Doctors),
                refered_staff = self.active_staff,
                status = True)
            
    def termination(self, status):
        empty_list = (status.select().count() == 0)
        if empty_list:
            print('No users to be found.\n')
            return True
        self.view_list(status, True)
        id = int(input("Enter the person's ID:\n"))
        person = status.get(status.id == id)
        person.status = False
        person.save()
        print("Person got terminated.(status to False)")
        
    def view_list(self, status, situation):
        empty_list = (status.select().count() == 0)
        if empty_list:
            print('No users to be found.\n')
            return True
        if status == Doctors:
            for i in status.select().where(status.status == situation):
                doctor_list = [f'{i.id}',
                    f'Work code: {i.work_code}',
                    f'First name: {i.first_name}',
                    f'Last name: {i.last_name}',
                    f'Department: {i.department}']
                print('\n'.join(doctor_list)) 
        elif status == Patients:
            for i in status.select().where(status.status == situation):
                patients_list = [f'{i.id}',
                    f'National ID: {i.national_id}',
                    f'First name: {i.first_name}',
                    f'Last name: {i.last_name}',
                    f'Age: {i.age}',
                    f'Refered Doctor: {i.refered_doctor}']
                print('\n'.join(patients_list))         
        elif status == Surgeryrooms:
            for i in status.select().where(status.status == situation):
                sr_list = [f'{i.id}',
                    f'Name: {i.name}',
                    f'Related Patient: {i.related_patient}',
                    f'Related Doctor: {i.related_doctor}',
                    f'Related Staff: {i.related_staff}']
                print('\n'.join(sr_list)) 
            
        
    def set_refered(self,status):
        print(f"Refering the {status.__name__}...")
        print("Enter the person's ID")
        while True:
            index = input()
            user = status.select().where(status.id == index)
            if not user.exists():
                print("Invalid ID, Try again\n")
            else:
                x = status.get(status.id == index)
                
                return x.id
    
    def banner(self):
        print("--------------------------------------------------")
        banner = [
            '-=-=-=-=-=-=-=-=-=-=-=-=-',
            f"Welcome aboard, Staff {self.active_staff.username}",
            '',
            '1.  View - available - Doctors ',
            '2.  View - available - Patients ',
            '3.  View - available - Surgery Rooms ',
            '',
            '4.  View - terminated - Doctors ',
            '5.  View - terminated - Patients ',
            '6.  View - terminated - Surgery Rooms ',
            '',
            '7.  Register a Doctor ',
            '8.  Register a Patients ',
            '9.  Register a Surgery Room ',
            '',
            '10.  Terminate a Doctor ',
            '11.  Terminate a Patients ',
            '12.  Terminate a Surgery Room ',
            '',
            '13. Exit',
            '-=-=-=-=-=-=-=-=-=-=-=-=-',
            '']  
        print('Navigate by entering the respective number:')
        
        while True:
            print('\n'.join(banner))
            inp = int(input())
            if inp == 1:
                self.view_list(Doctors, True)
            elif inp == 2:
                self.view_list(Patients, True)
            elif inp == 3:
                self.view_list(Surgeryrooms, True)
            elif inp == 4:
                self.view_list(Doctors, False)
            elif inp == 5:
                self.view_list(Patients, False)
            elif inp == 6:
                self.view_list(Surgeryrooms, False)
            elif inp == 7:
                self.registeration(Doctors)
            elif inp == 8:
                self.registeration(Patients)
            elif inp == 9:
                self.registeration(Surgeryrooms)              
            elif inp == 10:
                self.termination(Doctors)
            elif inp == 11:
                self.termination(Patients)
            elif inp == 12:
                self.termination(Surgeryrooms)
            elif inp == 13:
                exit()


app = Hospital()
app.login()

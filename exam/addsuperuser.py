from model import *

def register_staff():
    print('Welcome to registertaion site.\n')
    Staff.create(
        username = input("Enter the staff's username:\n"),
        first_name = input("Enter their first name:\n"),
        last_name = input("Enter their last name:\n"),
        password = int(input("Enter their password:\n")),
        status = True
    )
    print('Staff added to the database')


register_staff()
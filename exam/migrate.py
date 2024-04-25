from model import *
import os

def execute_db():
    if not os.path.exists(database_path):
        db.connect()
        db.create_tables([Staff, Patients, Doctors, Surgeryrooms ])
        
execute_db()
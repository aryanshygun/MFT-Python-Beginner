from peewee import *
database_path = 'Projects/MFT_FINAL/Hospital_database.db'
db = SqliteDatabase(database_path)

class BaseModel(Model):
    class Meta:
        database = db

class Staff(BaseModel):
    username = CharField(max_length= 16, unique = True, index = True)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    password = IntegerField()
    status = BooleanField()
    
class Doctors(BaseModel):
    work_code = IntegerField(unique = True)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    department = CharField(max_length=32)
    status = BooleanField()

class Patients(BaseModel):
    national_id = IntegerField(unique = True)
    first_name = CharField(max_length=32)
    last_name = CharField(max_length=32)
    age = IntegerField()
    refered_doctor = ForeignKeyField(Doctors, backref = 'patient', on_delete = 'CASCADE')
    status = BooleanField()


class Surgeryrooms(BaseModel):
    name = CharField(unique = True)
    refered_patient = ForeignKeyField(Patients, backref='surgeryrooms', on_delete='CASCADE')
    refered_doctor = ForeignKeyField(Doctors, backref='surgeryrooms', on_delete='CASCADE')
    refered_staff = ForeignKeyField(Staff, backref='surgeryrooms', on_delete='CASCADE')
    status = BooleanField()


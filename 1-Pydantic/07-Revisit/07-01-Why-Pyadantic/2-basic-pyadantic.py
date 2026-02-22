from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    weight: float

def insert_patient_date(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted patient data')


def update_patient_date(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Updated patient data')

patient = Patient(name='Pratap', age=30, weight=70.5)
insert_patient_date(patient)
update_patient_date(patient)
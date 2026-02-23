from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool = False
    allergies: List[str] = []
    contact_details: Dict[str, str] = {}


def insert_patient_date(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted patient data')


def update_patient_date(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Updated patient data')

patient = Patient(name='Pratap', age=30, weight=70.5, married=True, allergies=['Peanuts'], contact_details={'email': 'pratap@example.com', 'phone': '1234567890'})
insert_patient_date(patient)
update_patient_date(patient)
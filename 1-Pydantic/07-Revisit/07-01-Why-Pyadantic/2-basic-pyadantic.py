from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str = Field(max_length=50, description='Name of the patient')
    email: EmailStr = Field(..., description='Email of the patient')
    linkedInUrl: Optional[AnyUrl] = None
    age: int = Field(gt=0, lt=90, description='Age of the patient')
    weight: float = Field(gt=0, lt=120, description='Weight in kilograms')
    married: bool = Field(default=False, description='Married status')
    allergies: Optional[List[str]] = Field(None, max_length=5, description='List of allergies')
    contact_details: Dict[str, str] = Field({}, description='Contact details')


def insert_patient_date(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedInUrl)
    print(patient.age)
    print(patient.weight)
    print('Inserted patient data')


def update_patient_date(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedInUrl)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Updated patient data')

patient = Patient(name='Pratap', email='pratap@example.com', linkedInUrl='https://www.linkedin.com/in/pratap-padhy/', age=30, weight=1,  contact_details={'email': 'pratap@example.com', 'phone': '1234567890'})
insert_patient_date(patient)
update_patient_date(patient)
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, description='Name of the patient', example='Pratap')]
    email: Annotated[EmailStr, Field(..., description='Email of the patient', example='pratap@example.com')]
    linkedInUrl: Optional[AnyUrl] = None
    age: Annotated[int, Field(gt=0, lt=90, description='Age of the patient', example=30)]
    weight: Annotated[float, Field(gt=0, lt=120, strict=True, description='Weight in kilograms', example=70.5)]    
    married: Annotated[bool, Field(default=False, description='Married status', example=False)]
    allergies: Optional[List[str]] = Field(None, max_length=5, description='List of allergies', example=['Peanuts', 'Shellfish'])
    contact_details: Dict[str, str] = Field({}, description='Contact details', example={'email': 'pratap@example.com', 'phone': '1234567890'})

    @field_validator('weight', mode='before')
    def validate_weight(cls, v):
        if v < 0:
            raise ValueError('Weight cannot be negative')
        return v

    @field_validator('email')
    def validate_email(cls, v):
        valid_domains = ['hdfc', 'icici', 'axis']
        domain_name = v.split('@')[-1].split('.')[0]
        if not any(domain in domain_name for domain in valid_domains):
            raise ValueError('Invalid email address')
        return v

    @field_validator('name')
    def transform_name(cls, v):
        return v.upper()


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

patient = Patient(name='Pratap', email='pratap@hdfc.com', linkedInUrl='https://www.linkedin.com/in/pratap-padhy/', age=30, weight=70.5,  contact_details={'email': 'pratap@example.com', 'phone': '1234567890'}, allergies=['Peanuts'])
insert_patient_date(patient)
update_patient_date(patient)
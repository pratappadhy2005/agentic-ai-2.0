from pydantic import BaseModel, EmailStr, model_validator, computed_field
from typing import Annotated, List, Dict, Optional

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str

class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    address: Address

patient = Patient(name='Pratap', email='pratap@example.com', age=65, address=Address(street='123 Main St', city='Anytown', state='CA', zip='12345'))
print(patient)

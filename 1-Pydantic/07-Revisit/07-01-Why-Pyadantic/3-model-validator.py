from pydantic import BaseModel, field_validator, EmailStr, model_validator
from typing import Annotated, List, Dict, Optional

class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str] = []
    contact_details: Dict[str, str] = {}

    @model_validator(mode='after')
    def validate_patient(self):
        if self.age > 60 and self.weight < 60:
            raise ValueError('Weight must be at least 60 kg for age above 60')
        return self 

patient = Patient(name='Pratap', email='pratap@example.com', age=65, weight=50, married=False)
print(patient)

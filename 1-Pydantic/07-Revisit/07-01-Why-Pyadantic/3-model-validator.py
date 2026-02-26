from pydantic import BaseModel, EmailStr, model_validator, computed_field
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
    
    @computed_field
    def is_adult(self) -> bool:
        return self.age >= 18

    @computed_field
    def bmi(self) -> float:
        return self.weight / (self.age ** 2)

patient = Patient(name='Pratap', email='pratap@example.com', age=65, weight=70, married=False)
print(patient.is_adult)
print(patient.bmi)

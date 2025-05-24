from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str
    department: Optional[str] = Field(None, min_length=3, max_length=50)
    salary: float = Field(..., gt=1000)


employee_data = {
    "id": "1",
    "name": "John Doe",
    # "department": "Engineering",
    "salary": "5000"
}

employee = Employee(**employee_data)
print(employee)

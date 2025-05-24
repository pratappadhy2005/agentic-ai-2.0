from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    city: str
    country: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    joined: datetime
    addresses: List[Address]

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%Y-%m-%d")}
    )


user = User(
    id=1,
    name="John",
    joined=datetime(2024, 1, 1),
    addresses=[
        Address(city="New York", country="USA", zip_code="10001"),
        Address(city="San Francisco", country="USA", zip_code="94101")
    ]
)

# Using model_dump
print(user.model_dump())

print(user.model_dump_json())

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool = True


input_data = {
    "id": "1",
    "name": "John Doe",
    "is_active": 5
}

user = User(**input_data)
print(user)

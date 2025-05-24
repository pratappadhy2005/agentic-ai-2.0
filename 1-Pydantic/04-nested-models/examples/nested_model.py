from pydantic import BaseModel
from typing import List, Optional


class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    name: str
    age: int
    address: Optional[Address] = None
    addresses: List[Address] = []


class Comment(BaseModel):
    text: str
    user: User
    replies: Optional[List["Comment"]] = None


Comment.model_rebuild()

user = User(name="John", age=30, address=Address(
    city="New York", country="USA"))
print(user)

user = User(name="John", age=30, addresses=[
            Address(city="New York", country="USA")])

user1 = User(name="John", age=30, addresses=[
             {"city": "New York", "country": "USA"},
             {"city": "San Francisco", "country": "USA"}
             ])
print(user1)

comment = Comment(text="This is a comment", user=user)
print(comment)

comment1 = Comment(text="This is a comment", user=user, replies=[
    Comment(text="This is a reply", user=user1)
])
print(comment1)

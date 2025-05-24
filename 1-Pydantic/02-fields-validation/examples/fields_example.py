from pydantic import BaseModel
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    total: float
    discount: Dict[str, int] = {}


class BlogPost(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str] = []
    metadata: Dict[str, str] = {}
    published: Optional[bool] = False


cart_data = {
    "user_id": "1",
    "items": ["item1", "item2", "item3"],
    "total": "100.00",
    "discount": {"code": "879569", "amount": "10"}
}

blog_post_data = {
    "title": "My First Blog Post",
    "content": "This is my first blog post. I hope you like it!",
    "author": "John Doe",
    "tags": ["python", "pydantic", "validation"],
    "metadata": {"key1": "value1", "key2": "value2"},
    "published": True
}

cart = Cart(**cart_data)
print(cart)

blog_post = BlogPost(**blog_post_data)
print(blog_post)

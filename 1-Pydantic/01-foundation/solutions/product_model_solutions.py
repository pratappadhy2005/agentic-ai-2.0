from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    in_stock: bool = True


product_data = {
    "id": "1",
    "name": "Product 1",
    "price": "10.99",
    "quantity": "5",
    "in_stock": "True"
}

product = Product(**product_data)
print(product)

from pydantic import BaseModel

class ProductCreate(BaseModel):
  name: str
  price: float
  dimensions: str
  description: str

  class Config:
    orm_mode = True

class Product(ProductCreate):
  id: int
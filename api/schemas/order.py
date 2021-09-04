from pydantic import BaseModel
from typing import List, Optional

class Images(BaseModel):
  path: str

  class Config:
    orm_mode = True

class Categories(BaseModel):
  name: str

  class Config:
    orm_mode = True

class Product(BaseModel):
  id: int
  name: str
  price: Optional[float]
  dimensions: Optional[str]
  description: Optional[str]
  images: List[Images]
  categories: List[Categories]

  class Config:
    orm_mode = True

class Address(BaseModel):
  id: int
  street: str
  number: int
  complement: Optional[str]
  city: str
  state: str
  country: str

  class Config:
    orm_mode = True

class Association(BaseModel):
  products: Product
  quantity: int

  class Config:
      orm_mode = True

class Order(BaseModel):
  id: int
  ship_address: Optional[Address]
  products: List[Association]

  class Config:
    orm_mode = True
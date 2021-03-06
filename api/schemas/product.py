from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
  id: int
  username: str

  class Config:
    orm_mode = True
class Images(BaseModel):
  path: str

  class Config:
    orm_mode = True

class Categories(BaseModel):
  name: str

  class Config:
    orm_mode = True

class ProductDelete(BaseModel):
  detail: str

class ProductCreate(BaseModel):
  name: str
  price: Optional[float]
  dimensions: Optional[str]
  description: Optional[str]

  class Config:
    orm_mode = True

class Product(ProductCreate):
  id: int
  images: List[Images]
  categories: List[Categories]
  owner: User
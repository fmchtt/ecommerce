from pydantic import BaseModel
from typing import List, Optional

class Images(BaseModel):
  path: str

  class Config:
    orm_mode = True

class Product(BaseModel):
  name: str
  price: Optional[float]
  dimensions: Optional[str]
  description: Optional[str]
  images: List[Images]

  class Config:
    orm_mode = True

class CategoryCreate(BaseModel):
  name: str

  class Config:
    orm_mode = True

class Category(CategoryCreate):
  id: int

class CategoryVerbose(Category):
  products: List[Product]
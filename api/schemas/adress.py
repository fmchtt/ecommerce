from pydantic import BaseModel
from typing import List, Optional

class AddressCreate(BaseModel):
  street: str
  number: int
  complement: Optional[str]
  city: str
  state: str
  country: str

  class Config:
    orm_mode = True

class Address(AddressCreate):
  id: int
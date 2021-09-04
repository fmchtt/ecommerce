from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

class Address(Base):
  __tablename__ = "addresses"
  id = Column(Integer, primary_key=True, index=True)
  street = Column(String(200), nullable=False)
  number = Column(String(200), nullable=False)
  complement = Column(String(200))
  city = Column(String(200), nullable=False)
  state = Column(String(200), nullable=False)
  country = Column(String(200), nullable=False)
  user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
  user = relationship("User", back_populates="addresses")
  orders = relationship("Order", back_populates="ship_address")
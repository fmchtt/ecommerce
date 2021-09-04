from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.orm import relationship
from api.database import Base
from api.models import order_model

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    username = Column(String(50))
    hashed_password = Column(Text)
    avatar_url = Column(String(200), nullable=True)
    is_active = Column(Boolean, default=True)
    orders = relationship("Order", secondary=order_model.associative_table_user, back_populates="owner")
    addresses = relationship("Address", back_populates="user")
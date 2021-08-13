from sqlalchemy import Boolean, Column, Integer, String, Text
from api.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    username = Column(String(50))
    hashed_password = Column(Text)
    avatar_url = Column(String(200), nullable=True)
    is_active = Column(Boolean, default=True)
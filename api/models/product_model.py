from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from api.database import Base
from api.models import image_model, category_model

class Product(Base):
  __tablename__ = 'products'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(150), nullable=False)
  price = Column(Float)
  dimensions = Column(String(100))
  description = Column(Text)
  owner_id = Column(Integer, ForeignKey('users.id'), nullable=False, name="fk_product_user")
  images = relationship('Image', secondary=image_model.associative_table, back_populates="products")
  categories = relationship("Category", secondary=category_model.associative_table, back_populates="products")
  orders = relationship("AssociationOrderProduct", back_populates="products")
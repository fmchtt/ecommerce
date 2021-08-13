from sqlalchemy import Boolean, Column, Integer, String, Text, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

associative_table = Table("association_image_product", Base.metadata, 
  Column("id",Integer, primary_key=True, index=True),
  Column('product_id', Integer, ForeignKey('products.id')),
  Column('image_id', Integer, ForeignKey('images.id'))
)

class Image(Base):
  __tablename__ = 'images'

  id = Column(Integer, primary_key=True, index=True)
  path = Column(Text)
  products = relationship("Product", secondary=associative_table, back_populates="images")
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

associative_table = Table("association_category_product", Base.metadata, 
  Column("id",Integer, primary_key=True, index=True),
  Column('product_id', Integer, ForeignKey('products.id')),
  Column('category_id', Integer, ForeignKey('categories.id'))
)

class Category(Base):
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(50), nullable=False)
  products = relationship("Product", secondary=associative_table, back_populates="categories")
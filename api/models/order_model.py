from sqlalchemy import Column, Integer, Table, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from api.database import Base
from datetime import datetime

associative_table_user = Table("association_order_user", Base.metadata, 
  Column("id",Integer, primary_key=True, index=True),
  Column('users_id', Integer, ForeignKey('users.id')),
  Column('order_id', Integer, ForeignKey('orders.id'))
)

class AssociationOrderProduct(Base):
  __tablename__ = "association_order_product"

  id = Column(Integer, primary_key=True, index=True)
  product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
  order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
  quantity = Column(Integer, default=1, nullable=False)
  products = relationship("Product", back_populates="orders")
  orders = relationship("Order", back_populates="products")

class Order(Base):
  __tablename__ = "orders"
  id = Column(Integer, primary_key=True, index=True)
  date = Column(Date, nullable=False, default=datetime.now())
  finalized = Column(Boolean, default=False)
  ship_address_id = Column(Integer, ForeignKey("addresses.id"), nullable=True, name="fk_order_adress")
  owner_id = Column(Integer, ForeignKey('users.id'), nullable=False, name="fk_order_user")
  ship_address = relationship("Address", back_populates="orders")
  products = relationship("AssociationOrderProduct", back_populates="orders")
  owner = relationship("User", secondary=associative_table_user, back_populates="orders")
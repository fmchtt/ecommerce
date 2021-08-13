from sqlalchemy.orm import Session
from api.schemas.product import ProductCreate
from api.models.product_model import Product
from api.models.category_model import Category

def listar_produtos(db: Session):
  return db.query(Product).all()

def criar_produto(product: ProductCreate, db: Session):
  product_new = Product(name=product.name, price=product.price, dimensions=product.dimensions, description=product.description)
  db.add(product_new)
  db.commit()
  db.refresh(product_new)
  return product_new
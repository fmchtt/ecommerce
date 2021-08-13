from sqlalchemy.orm import Session
from api.models.category_model import Category

def listar_categorias(db: Session):
  return db.query(Category).all()

def criar_categoria(name: str, db: Session):
  category = Category(name=name)
  db.add(category)
  db.commit()
  db.refresh(category)
  return category
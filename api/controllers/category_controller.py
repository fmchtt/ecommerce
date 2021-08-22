from sqlalchemy.orm import Session
from api.models.category_model import Category
from fastapi import HTTPException

def listar_categorias(db: Session):
  return db.query(Category).all()

def criar_categoria(name: str, db: Session):
  category = Category(name=name)
  db.add(category)
  db.commit()
  db.refresh(category)
  return category

def buscar_categoria(category_id: int, url: str, db: Session):
  category = db.query(Category).filter(Category.id == category_id).first()

  if not category:
    raise HTTPException(404, "Categoria não encontrada")

  for product in category.products:
    for image in product.images:
      image.path = f"{url}{image.path}"

  return category
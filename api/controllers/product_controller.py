from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from api.schemas.product import ProductCreate
from api.models.product_model import Product
from api.models.category_model import Category
from api.models.image_model import Image
from api.services.files import save_file, delete_file
from fastapi import UploadFile

def listar_produtos(url: str, db: Session):
  products = db.query(Product).all()

  for product in products:
    for image in product.images:
      image.path = f"{url}{image.path}"
  
  return products

def criar_produto(name: str, price: float, dimensions: str, description: str, owner_id: int, db: Session, images: List[UploadFile] = []):
  product_new = Product(name=name, price=price, dimensions=dimensions, description=description, owner_id=owner_id)

  for image in images:
    img_path = save_file(image)
    img = Image(path=img_path)
    product_new.images.append(img)

  db.add(product_new)
  db.commit()
  db.refresh(product_new)
  return product_new

def deletar_produto(product_id: int, user_id: int, db: Session):
  product = db.query(Product).filter(Product.id == product_id).first()
  
  if not product:
    raise HTTPException(404, "Produtos não encontrado!")

  if product.owner_id != user_id:
    raise HTTPException(401, "Somente o criador do produto pode remover!")

  for image in product.images:
    delete_file(image.path)

  db.delete(product)
  db.commit()

  return {"detail": "Produto deletado com sucesso!"}
from typing import List
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from api.models import Product, Category, Image
from api.services.files import save_file, delete_file
from fastapi import UploadFile

def listar_produtos(url: str, page: int, db: Session, p: str = None):
  if page > 1:
    offset = (page - 1) * 20
  else:
    offset = 0
    
  products = db.query(Product).order_by(Product.id.desc()).offset(offset).limit(20).all()

  for product in products:
    for image in product.images:
      image.path = f"{url}{image.path}"
  
  return products

def buscar_produto(product_id: int, url: str, db: Session):
  product = db.query(Product).filter(Product.id == product_id).first()

  if not product:
    raise HTTPException(404, "Produto não encontrado!")

  for image in product.images:
    image.path = f"{url}{image.path}"

  return product

def listar_produtos_usuario(page: int, user_id: int, db: Session, url: str):
  if page > 1:
    offset = (page - 1) * 20
  else:
    offset = 0
    
  products = db.query(Product).filter(Product.owner_id == user_id).order_by(Product.id.desc()).offset(offset).limit(20).all()

  for product in products:
    for image in product.images:
      image.path = f"{url}{image.path}"
  
  return products

def criar_produto(name: str, price: float, dimensions: str, description: str, url: str, owner_id: int, db: Session, images: List[UploadFile] = []):
  product_new = Product(name=name, price=price, dimensions=dimensions, description=description, owner_id=owner_id)

  for image in images:
    img_path = save_file(image)
    img = Image(path=img_path)
    product_new.images.append(img)

  db.add(product_new)
  db.commit()
  db.refresh(product_new)

  for image in product_new.images:
    image.path = f"{url}{image.path}"

  return product_new

def adicionar_categoria_produto(product_id: int, category_id: int, user_id: int, db: Session):
  product = db.query(Product).filter(Product.id == product_id).first()
  category = db.query(Category).filter(Category.id == category_id).first()

  if not product or not category:
    raise HTTPException(404, "Produto ou categoria não encontrado")

  if product.owner_id != user_id:
    raise HTTPException(401, "Somente o criador do produto pode adicionar categorias")

  product.categories.append(category)
  db.commit()
  db.refresh(product)
  return product
  


def deletar_produto(product_id: int, user_id: int, db: Session):
  product = db.query(Product).filter(Product.id == product_id).first()
  
  if not product:
    raise HTTPException(404, "Produtos não encontrado!")

  if product.owner_id != user_id:
    raise HTTPException(401, "Somente o criador do produto pode remover!")

  for image in product.images:
    try:
      delete_file(image.path)
    except FileNotFoundError:
      print("Tentativa de delete em arquivo nao encontrado")

  db.delete(product)
  db.commit()

  return {"detail": "Produto deletado com sucesso!"}
from typing import List
from fastapi import APIRouter, Depends, Form, UploadFile, File, Request
from fastapi_jwt_auth import AuthJWT
from api.database import SessionLocal
from sqlalchemy.orm import Session
from api.schemas.product import ProductCreate, Product, ProductDelete
from api.controllers import product_controller

def get_db() -> Session:
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

routes = APIRouter(prefix="/products")

@routes.post("/", response_model=Product)
def criar_produto(request: Request, name: str = Form(...), price: float = Form(None), dimensions: str = Form(None), description: str = Form(None), images: List[UploadFile] = File(None), db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  return product_controller.criar_produto(name, price, dimensions, description, Authorize.get_jwt_subject(), db, images)

@routes.get("/", response_model=List[Product])
def listar_produtos(request: Request, db: Session = Depends(get_db)):
  return product_controller.listar_produtos(request.base_url, db)

@routes.delete("/{product_id}/", response_model=ProductDelete)
def deletar_imagem(product_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return product_controller.deletar_produto(product_id, Authorize.get_jwt_subject(), db)
from typing import List
from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from api.database import SessionLocal
from sqlalchemy.orm import Session
from api.schemas.product import ProductCreate, Product
from api.controllers import product_controller

def get_db() -> Session:
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

routes = APIRouter(prefix="/products")

@routes.post("/", response_model=Product)
def criar_produto(product: ProductCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  return product_controller.criar_produto(product, db)

@routes.get("/", response_model=List[Product])
def listar_produtos(db: Session = Depends(get_db)):
  return product_controller.listar_produtos(db)
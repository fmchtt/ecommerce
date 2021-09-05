from typing import List, Optional
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


@routes.get("/", response_model=List[Product])
def listar_produtos(request: Request, p: Optional[str] = None, page: Optional[int] = 1, db: Session = Depends(get_db)):
  return product_controller.listar_produtos(request.base_url, page, db, p)

@routes.get("/{product_id}/", response_model=Product)
def buscar_produto(product_id: int, request: Request, db: Session = Depends(get_db)):
  return product_controller.buscar_produto(product_id, request.base_url, db)

@routes.get("/created/me/", response_model=List[Product])
def listar_produtos_criados_pelo_usuario(request: Request, page: Optional[int] = 1, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  return product_controller.listar_produtos_usuario(page, Authorize.get_jwt_subject(), db, request.base_url)

@routes.post("/", response_model=Product)
def criar_produto(request: Request, name: str = Form(...), price: float = Form(None), dimensions: str = Form(None), description: str = Form(None), images: List[UploadFile] = File(None), db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  return product_controller.criar_produto(name, price, dimensions, description, request.base_url, Authorize.get_jwt_subject(), db, images)

@routes.patch("/add/{product_id}/category/{category_id}/", response_model=Product)
def adicionar_categoria(product_id: int, category_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return product_controller.adicionar_categoria_produto(product_id, category_id, Authorize.get_jwt_subject(), db)

@routes.delete("/{product_id}/", response_model=ProductDelete)
def deletar_produto(product_id: int, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
  Authorize.jwt_required()
  return product_controller.deletar_produto(product_id, Authorize.get_jwt_subject(), db)
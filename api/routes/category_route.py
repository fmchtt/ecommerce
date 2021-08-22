from typing import List
from fastapi import APIRouter, Depends, Request
from fastapi_jwt_auth import AuthJWT
from api.schemas.category import Category, CategoryCreate, CategoryVerbose
from api.database import SessionLocal
from sqlalchemy.orm import Session
from api.controllers import category_controller

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

routes = APIRouter(prefix="/category")

@routes.get("/", response_model=List[Category])
def listar_categorias(db: Session = Depends(get_db)):
    return category_controller.listar_categorias(db)

@routes.get("/{category_id}/", response_model=CategoryVerbose)
def buscar_categoria(category_id: int, request: Request, db: Session = Depends(get_db)):
    return category_controller.buscar_categoria(category_id, request.base_url, db)


@routes.post("/", response_model=Category)
def criar_categoria(category: CategoryCreate, db: Session = Depends(get_db), Authorize: AuthJWT = Depends()):
  Authorize.jwt_required()
  return category_controller.criar_categoria(category.name, db)
from fastapi import APIRouter
from api.routes import auth_route, user_route, category_route, product_route, address_route, order_route

routes = APIRouter(prefix="/api")

routes.include_router(auth_route.auth_routes, tags=["Autenticação"])
routes.include_router(user_route.user_routes, tags=["Usuário"])
routes.include_router(category_route.routes, tags=["Categoria"])
routes.include_router(product_route.routes, tags=["Produto"])
routes.include_router(address_route.routes, tags=["Endereço"])
routes.include_router(order_route.routes, tags=["Pedidos"])

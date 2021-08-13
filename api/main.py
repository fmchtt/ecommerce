from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api.router import routes
from fastapi_jwt_auth.exceptions import AuthJWTException
from api.schemas.auth import Settings
from fastapi_jwt_auth import AuthJWT
from api.database import Base, engine
import os
import inspect, re
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ECommerce API")

app.add_middleware(CORSMiddleware, allow_origins=['*'],allow_methods=["*"],allow_headers=["*"])

if not os.path.exists('uploads'):
  os.mkdir('uploads')
  
app.mount("/uploads", StaticFiles(directory="uploads"), name="static")

@AuthJWT.load_config
def get_config():
    return Settings()

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": "Não Autorizado!"}
    )

app.include_router(routes)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ecommerce API",
        version="0.2.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }

    cookie_security_schemes = {
        "AuthJWTCookieAccess": {
            "type": "apiKey",
            "in": "header",
            "name": "X-CSRF-TOKEN"
        },
        "AuthJWTCookieRefresh": {
            "type": "apiKey",
            "in": "header",
            "name": "X-CSRF-TOKEN"
        }
    }
    refresh_token_cookie = {
        "name": "refresh_token_cookie",
        "in": "cookie",
        "required": False,
        "schema": {
            "title": "refresh_token_cookie",
            "type": "string"
        }
    }
    access_token_cookie = {
        "name": "access_token_cookie",
        "in": "cookie",
        "required": False,
        "schema": {
            "title": "access_token_cookie",
            "type": "string"
        }
    }

    if "components" in openapi_schema:
        openapi_schema["components"].update({"securitySchemes": cookie_security_schemes})
    else:
        openapi_schema["components"] = {"securitySchemes": cookie_security_schemes}

    api_router = [route for route in app.routes if isinstance(route, APIRoute)]

    for route in api_router:
        path = getattr(route, "path")
        endpoint = getattr(route,"endpoint")
        methods = [method.lower() for method in getattr(route, "methods")]

        for method in methods:
            # access_token
            if (
                re.search("jwt_required",inspect.getsource(endpoint)) or
                re.search("fresh_jwt_required",inspect.getsource(endpoint)) or
                re.search("jwt_optional",inspect.getsource(endpoint))
            ):
                try:
                    openapi_schema["paths"][path][method]['parameters'].append(access_token_cookie)
                except Exception:
                    openapi_schema["paths"][path][method].update({"parameters":[access_token_cookie]})

                # method GET doesn't need to pass X-CSRF-TOKEN
                if method != "get":
                    openapi_schema["paths"][path][method].update({
                        'security': [{"AuthJWTCookieAccess": []}]
                    })

            # refresh_token
            if re.search("jwt_refresh_token_required",inspect.getsource(endpoint)):
                try:
                    openapi_schema["paths"][path][method]['parameters'].append(refresh_token_cookie)
                except Exception:
                    openapi_schema["paths"][path][method].update({"parameters":[refresh_token_cookie]})

                # method GET doesn't need to pass X-CSRF-TOKEN
                if method != "get":
                    openapi_schema["paths"][path][method].update({
                        'security': [{"AuthJWTCookieRefresh": []}]
                    })

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
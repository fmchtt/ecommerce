from pydantic import BaseModel

class Settings(BaseModel):
    authjwt_secret_key: str = "61cf5d460e1230c9f34f57849f8f8d58"
    authjwt_token_location: set = {"cookies"}
    authjwt_cookie_csrf_protect: bool = True
    authjwt_cookie_samesite: str = "strict"

class Login(BaseModel):
    detail: str
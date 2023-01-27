from starlette.config import Config


config = Config(".env")
DATABASE_URL = config('EE_DATABASE_URL', cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = 'HS256'
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="e5f5c20901d644a921b92a860d127310b54f4d82661c21556b534cf1f0606648")
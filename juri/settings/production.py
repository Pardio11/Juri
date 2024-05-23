from .base import *
from dotenv import load_dotenv
import os
load_dotenv()

DEBUG = False

ALLOWED_HOST_APP = os.getenv('ALLOWED_HOST_APP')
ALLOWED_HOSTS = [ALLOWED_HOST_APP]

CSRF_TRUSTED_ORIGINS = ['https://' + ALLOWED_HOST_APP]
CORS_ALLOWED_ORIGINS = ['https://' + ALLOWED_HOST_APP]

SESSION_COOKIE_SECURE = True 
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSP_DEFAULT_SRC = ("'self'",)


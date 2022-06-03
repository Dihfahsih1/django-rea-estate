

from pathlib import Path
import environ
env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
SITE_ID=1

THIRD_PARTY_APPS=[
    "rest_framework",
    "django_filters",
    "django_countries",
    "phonenumber_field",
    "djoser",
    "rest_framework_simplejwt",
    
]

LOCAL_APPS=[
   "apps.common",
   "apps.users",
   "apps.profiles",
   "apps.ratings",
   "apps.properties",
   "apps.enquiries",
  
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'real_estate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'real_estate.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/staticfiles/'

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIR = []
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = BASE_DIR / "mediafiles"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User" #custom user model.

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":(
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES":(
        "rest_framework.permissions.IsAdminUser" #just added this to fix the bug
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES":(
        "Bearer",  
        "JWT",
    ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),#in production make the minutes as short as possible like 10 mins
    'REFRESH_TOKEN_LIFETIME':timedelta(days=1),
    'SIGNING_KEY':env("SIGNING_KEY"),
    'AUTH_HEADER_NAME':"HTTP_AUTHORIZATON",
    'AUTH_TOKEN_CLASSES':("rest_framework_simplejwt.tokens.AccessToken",),
    }
DJOSER ={
    "LOGIN_FIELD":"username",
    "USER_CREATE_PASSWORD_RETYPE":True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION":True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION":True,
    "SEND_CONFIRMATION_EMAIL":True,
    "PASSWORD_RESET_CONFIRM_URL":'password/reset/confirm/{uid}/{token}',
    "SET_PASSWORD_RETYPE":True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL":'email/reset/confirm/{uid}/{token}',
    "ACTIVATION_URL":'activate/{uid}/{token}',
    "SEND_ACTIVATION_EMAIL":True,
    "SERIALIZERS":{
        "user_create":'apps.users.serializers.CreateUserSerializer,',
        "users":'apps.users.serializers.UserSerializer',
        "current_user":'apps.users.serializers.UserSerializer',
        "user_delete":'djoser.serializers.UserDeleteSerializer',
    }
    
    
} 

import logging
import logging.config
from django.utils.log import DEFAULT_LOGGING

logger = logging.getLogger(__name__)#create logger instance

LOG_LEVEL='INFO'

logging.config.dictConfig({
    "version":1,
    "disable_existing_loggers":False,
    "formatters":{
        "console":{
            "format":"%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
        },
        "file":{"format":"%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
        "django.server":DEFAULT_LOGGING["formatters"]["django.server"]
    },
    "handlers":{
        "console":{
            "class":"logging.StreamHandler",
            "formatter":"console",
        },
        "file":{
            "level":"INFO",
            "class":"logging.FileHandler",
            "formatter":"file",
            "filename":"logs/real_estate.log"
        },
        
        "django.server":DEFAULT_LOGGING["handlers"]["django.server"]
        
    },
    "loggers":{
        "":{"level":"INFO", "handlers":["console","file"],"propagate":False},
        "apps":{
            "level":"INFO","handlers":["console"],"propagate":False
        },
        "django.server":DEFAULT_LOGGING["loggers"]["django.server"]
        
    }
    
})

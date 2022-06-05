from .base import *

DATABASES = {
    'default': {
        'ENGINE':env("ENGINE"),
        'NAME':env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD':env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT':env("DB_PORT"),
    }
}

MAIL_USER=env("EMAIL_HOST_USER")
MAIL_HOST=env("EMAIL_HOST")
MAIL_PASSWORD=env("EMAIL_HOST_PASSWORD")
EMAIL_BACKEND=env("EMAIL_BACKEND")
EMAIL_USE_SSL=env("EMAIL_USE_SSL")
EMAIL_PORT=env("EMAIL_PORT")
DOMAIN=env("DOMAIN")
SITENAME="RealEstate"
DEFAULT_FROM_EMAIL=MAIL_USER
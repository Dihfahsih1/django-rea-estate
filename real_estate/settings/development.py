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

MAIL_USER=env("MAIL_USER")
MAIL_HOST=env("MAIL_HOST")
MAIL_PASSWORD=env("MAIL_PASSWORD")
EMAIL_BACKEND=env("EMAIL_BACKEND")

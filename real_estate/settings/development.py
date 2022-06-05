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
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST=env("EMAIL_HOST")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=True
EMAIL_PORT=env("EMAIL_PORT")
DEFAULT_FROM_EMAIL="info@real-estate.com"
DOMAIN=env("DOMAIN")
SITENAME="RealEstate"
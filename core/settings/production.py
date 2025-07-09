from .settings import *

SECRET_KEY = "acnj219in djisnc-i1nmpj_JINOI*UYG)Hjibspdnf02jioeh-01i2jfei!((&BHGVIUBHBVJY|TYGIUYGO*&UHOI))"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "10.82.27.73"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prodline",
        "USER": "postgres",
        "PASSWORD": "N47ur4@#2025",
        "HOST": "10.82.27.120",
        "PORT": "5432",
    }
}

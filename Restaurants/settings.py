"""
Django settings for Restaurants project.OA

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages

# Changing Error constant
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Redirect url
LOGIN_URL = '/login'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!djmcpg$vwpzu!a)i9&b0!44f-_lax$=chloacz!v*pv34hkn5"

# SECURITY WARNING: don't run with debug turned on in production
DEBUG = 1

ALLOWED_HOSTS = ['127.0.0.1', '34.217.50.171']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "home",
    "dashboard",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Restaurants.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Restaurants.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": 'myrestaurant',  # os.environ.get('NAME'),
            "USER": 'admin',  # os.environ.get('USER'),
            "PASSWORD": '12345678',  # os.environ.get('PASSWORD'),
            # os.environ.get('HOST'),
            "HOST": 'mysql-res.c4ctuc8g0dxj.us-west-2.rds.amazonaws.com',
            "PORT": '3306',  # os.environ.get('PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# S3 BUCKET CONFIG

AWS_ACCESS_KEY_ID = 'AKIAS6ENUTQNOTQ45WWF'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'mydjango-static-bucket'

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

AWS_QUERYSTRING_AUTH = False

AWS_LOCATION = 'static'

AWS_HEADERS = {'Access-Control-Allow-Origin': '*', }

AWS_DEFAULT_ACL = 'public-read'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

# 'https://mydjango-static-bucket.s3.amazonaws.com/media/'
MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / "media/"

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

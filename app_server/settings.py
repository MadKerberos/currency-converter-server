"""
Django settings for app_server project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.core.management.utils import get_random_secret_key

# True if not in os.environ
DEBUG = os.getenv("DEBUG", "True") == "True"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

#ALLOWED_HOSTS = env.str('DJANGO_ALLOWED_HOSTS', default='*').split(',')
ALLOWED_HOSTS = ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")


# Application definition
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    #Third Part Apps
    'rest_framework',
    'rest_framework.authtoken'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', 
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'app_server.urls'

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

WSGI_APPLICATION = 'app_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            # 'format':'[{server_time}] {message}',
            'format': '[{levelname}] [{asctime}] [{module}] [Message: {message}] ',
            'style': '{',
        },
        # 'formatter_request': {
        #     # 'format':'[{server_time}] {message}',
        #     'format': '[{levelname}] [{asctime}] [{module}] [Message: {message}] [{request}]',
        #     'style': '{',
        # },

    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'console_django_request': {
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'formatter_request'
        # },
    },
    'loggers': {
        # root level
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
        #django messages
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_files")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# MAIL HOST
# EMAIL_BACKEND = env('EMAIL_BACKEND')
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env('EMAIL_PORT')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = env('EMAIL_USE_TLS')

CORS_ALLOW_ALL_ORIGINS = True
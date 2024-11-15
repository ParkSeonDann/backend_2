"""
Django settings for shubik_shop project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from os.path import join
import os
from os.path import join

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.integration_type import IntegrationType


# Configurar Transbank manualmente para el entorno de pruebas
Transaction.commerce_code = "597055555532"
Transaction.api_key = "597055555532"
Transaction.integration_type = IntegrationType.TEST

# Configuración de Twilio
TWILIO_ACCOUNT_SID = 'ACec92be4dcf1e8fe6a1be53891ee58e77'
TWILIO_AUTH_TOKEN = '95f9bfdfac062d3a0b2ac3c659d2cefd'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'  # Número de WhatsApp del sandbox de Twilio

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#ax-5eq$oz*^#p$_c9^@og#)=5@rg7#ms3e_w&^fyy+n+h1)dt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'compras',
    'usuario',  # Cambia esto para activar las señales
    'productos',
    'tiendas',
    'rest_framework',
    'corsheaders',
    'django_filters',
    'rest_framework_simplejwt.token_blacklist',
    'login',
    'notificacion',
    'pagos',
    'sslserver',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    
]

CORS_ALLOW_ALL_ORIGINS = True  # Permitir todos los orígenes

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",  # Agregar también como origen confiable para CSRF
]

ROOT_URLCONF = 'shubik_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'vistas')
        ],
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

WSGI_APPLICATION = 'shubik_shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#
#respaldo de la base de datos
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'shubik',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': '190.44.152.202',  # o la dirección de tu servidor de base de datos
#         'PORT': '5432',       # puerto por defecto de PostgreSQL
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shubik',  # El nombre de tu base de datos
        'USER': 'postgres',
        'PASSWORD': '1234567890.a',
        'HOST': 'shubik.postgres.database.azure.com',
        'PORT': '5432',  # Puerto por defecto
        'OPTIONS': {
            'sslmode': 'require',  # Opcional, pero recomendado para mayor seguridad
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15), # Duración del token de acceso
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1), # Duración del token de refresh
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY, # Usamos el SECRET_KEY de tu configuración
    'AUTH_HEADER_TYPES': ('Bearer',), # Los tokens JWT se envían en los headers como 'Bearer <token>'
}


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuración de los archivos estáticos
STATIC_URL = '/static/'

# STATICFILES_DIRS es para rutas de archivos estáticos en desarrollo.
# Si tus archivos están en 'static', úsalo aquí.
STATICFILES_DIRS = [
    join(BASE_DIR, "static"),  # Carpeta que contiene tus archivos estáticos en desarrollo
]

# STATIC_ROOT solo se usa para producción. Define una carpeta diferente para evitar conflictos.
STATIC_ROOT = join(BASE_DIR, 'staticfiles')  # Carpeta donde `collectstatic` copiará los archivos


# URL y directorio de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Esto es para los filtros
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

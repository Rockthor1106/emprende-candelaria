import os
import dj_database_url
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-simple-key-for-lambda')

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'  

HOST = os.environ.get('HOST', 'http://127.0.0.1:8000')

ALLOWED_HOSTS = ['*']

IS_LAMBDA = os.environ.get('AWS_EXECUTION_ENV') is not None

AUTH_USER_MODEL = 'users.User' 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    'haztever',

    'haztever.business.apps.BusinessConfig',
    'haztever.catalog.apps.CatalogConfig',
    'haztever.reviews.apps.ReviewsConfig',
    'haztever.users.apps.UsersConfig',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'drf_spectacular',
    
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'haztever.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'haztever.wsgi.application'

if IS_LAMBDA:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
            ssl_require=True
        )  
    }
    
    # En caso de querer usar aurora
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'postgres'),
            'USER': os.environ.get('DB_USER', 'postgres'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', '5432'),
            'OPTIONS': {
                'connect_timeout': 10,
            },
        }
    }
    
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
    AWS_SIGNATURE_VERSION = 's3v4'
    AWS_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    STATIC_URL = f'https://{AWS_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_CUSTOM_DOMAIN}/media/'
    
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        },
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'media'

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
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_HMAC = False
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'account_confirm_email'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'account_confirm_email'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

REST_AUTH = {
    'LOGIN_SERIALIZER': 'haztever.users.serializers.CustomLoginSerializer',
    'REGISTER_SERIALIZER': 'haztever.users.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'haztever.users.serializers.CustomUserDetailsSerializer'
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# Configurar logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {
        "django.request": {"handlers": ["console"], "level": "ERROR"},
        "django": {"handlers": ["console"], "level": "ERROR"},
    },
}

# Email backend que loggea en lugar de enviar
if IS_LAMBDA:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT = int(os.environ.get("EMAIL_PORT", "587"))
    EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"] 
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", EMAIL_HOST_USER)

    # AGREGAR CONFIGURACIÓN DE SPECTACULAR PARA LAMBDA
    SPECTACULAR_SETTINGS = {
        'TITLE': 'Emprende Candelaria API',
        'DESCRIPTION': 'API para la plataforma Emprende Candelaria',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,
        'SWAGGER_UI_SETTINGS': {
            'deepLinking': True,
            'persistAuthorization': True,
        },
        'SERVERS': [
            {
                'url': HOST,
            }
        ]
    }
    
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    
    SPECTACULAR_SETTINGS = {
        'TITLE': 'Emprende Candelaria API',
        'DESCRIPTION': 'API para la plataforma Emprende Candelaria',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,
        'SWAGGER_UI_SETTINGS': {
            'deepLinking': True,
            'persistAuthorization': True,
        },
        'SERVERS': [
            {
                'url': 'http://127.0.0.1:8000',
            }
        ]
    }
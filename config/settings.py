"""
Django settings for Bright Looks project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-thiamstreetwear-secret-key-change-in-production-2024'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Third party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # Local apps
    'apps.store',
    'apps.orders',
    'apps.accounts',
    'apps.payments',
    'apps.dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.store.context_processors.cart_count',
                'apps.store.context_processors.categories_menu',
                'apps.store.context_processors.boutique_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database — MySQL via phpMyAdmin (port 3308)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'boutik',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3308',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Dakar'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/compte/connexion/'

# Allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Email (développement)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'thiambusiness44@gmail.com'

# Session cart
CART_SESSION_ID = 'cart'

# Business info
BOUTIQUE_TEL = '77 212 43 19'
BOUTIQUE_EMAIL = 'thiambusiness44@gmail.com'
BOUTIQUE_LOCATION = 'Ouest Foire, Dakar, Sénégal'
BOUTIQUE_PLUS_CODE = 'QG4H+4F9'
BOUTIQUE_MAPS_LAT = 14.7520
BOUTIQUE_MAPS_LNG = -17.4497
BOUTIQUE_MAPS_URL = (
    'https://www.google.com/maps/search/?api=1&query=QG4H%2B4F9%2C+Ouest+Foire%2C+Dakar%2C+S%C3%A9n%C3%A9gal'
)
BOUTIQUE_MAPS_EMBED = (
    'https://www.google.com/maps?q=QG4H%2B4F9%2C+Ouest+Foire%2C+Dakar%2C+S%C3%A9n%C3%A9gal'
    '&hl=fr&z=17&output=embed'
)
BOUTIQUE_ADRESSES = ['Ouest Foire']
BOUTIQUE_HORAIRES = 'Lundi – Samedi : 9h00 – 19h00'
WHATSAPP_NUMBER = '221772124319'
WHATSAPP_URL = 'https://wa.me/221772124319'
INSTAGRAM_URL = 'https://www.instagram.com/bright_look_221/'
SNAPCHAT_URL = 'https://www.snapchat.com/add/elzobright'

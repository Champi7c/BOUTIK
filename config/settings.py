"""
Django settings for ThiamStreetwear project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-thiamstreetwear-secret-key-change-in-production-2024')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

CSRF_TRUSTED_ORIGINS = [
    'http://thiamstreetwear.com',
    'https://thiamstreetwear.com',
    'http://www.thiamstreetwear.com',
    'https://www.thiamstreetwear.com',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
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
                'apps.store.context_processors.wishlist_ids',
                'apps.store.context_processors.boutique_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database — MySQL en production, SQLite en local
if os.environ.get('DB_HOST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'boutik_db'),
            'USER': os.environ.get('DB_USER', 'boutik_user'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'db'),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
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
ACCOUNT_LOGIN_METHODS = {'username', 'email'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Email (développement)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'thiambusiness44@gmail.com'

# Session cart
CART_SESSION_ID = 'cart'

# Stripe — remplace par tes vraies clés depuis dashboard.stripe.com
STRIPE_PUBLISHABLE_KEY = 'pk_test_REMPLACE_PAR_TA_CLE_PUBLIQUE'
STRIPE_SECRET_KEY = 'sk_test_REMPLACE_PAR_TA_CLE_SECRETE'
STRIPE_WEBHOOK_SECRET = 'whsec_REMPLACE_PAR_TON_SECRET_WEBHOOK'
STRIPE_CURRENCY = 'xof'  # Franc CFA — ou 'eur' si XOF non disponible sur ton compte

# Business info
BOUTIQUE_TEL = '78 530 98 74'
BOUTIQUE_EMAIL = 'thiambusiness44@gmail.com'
BOUTIQUE_LOCATION = 'Guediawaye & Colobane, Dakar, Sénégal'
BOUTIQUE_PLUS_CODE = ''
BOUTIQUE_MAPS_URL = (
    'https://www.google.com/maps/search/?api=1&query=Guediawaye%2C+Dakar%2C+S%C3%A9n%C3%A9gal'
)
BOUTIQUE_MAPS_EMBED = (
    'https://www.google.com/maps?q=Guediawaye%2C+Dakar%2C+S%C3%A9n%C3%A9gal'
    '&hl=fr&z=14&output=embed'
)
BOUTIQUE_ADRESSES = ['Guediawaye', 'Colobane']
BOUTIQUE_HORAIRES = 'Lundi – Samedi : 9h00 – 19h00'
# SEO / SEA — remplis dans .env
SITE_URL = os.environ.get('SITE_URL', 'https://thiamstreetwear.com')
GTM_ID = os.environ.get('GTM_ID', '')            # ex: GTM-XXXXXXX
META_PIXEL_ID = os.environ.get('META_PIXEL_ID', '')  # ex: 1234567890

WHATSAPP_NUMBER = '221785309874'
WHATSAPP_URL = 'https://wa.me/221785309874'
INSTAGRAM_URL = 'https://www.instagram.com/thiamstreetwear/'
SNAPCHAT_URL = 'https://www.snapchat.com/add/thiamstreetwear'

from pathlib import Path
from decouple import config
from csp.constants import SELF
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True

    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True


ALLOWED_HOSTS = ["localhost", "muelthaler.com", "www.muelthaler.com"]
REMOVE_WWW = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_minify_html',

    'base',
    'captcha',
    'goal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'personal-webpage.middleware.RemoveWWWMiddleware',
    'django_minify_html.middleware.MinifyHtmlMiddleware'
]

ROOT_URLCONF = 'personal-webpage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates']
        ,
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

WSGI_APPLICATION = 'personal-webpage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': config('SQLITE_PATH', default=str(BASE_DIR / 'db.sqlite3')),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_ROOT = BASE_DIR / "productionfiles"
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSP OPTIONS:
CONTENT_SECURITY_POLICY = {
    "DIRECTIVES": {
        "default-src": [SELF, "data:"],
        "img-src": [SELF],
        "script-src": [SELF],
        "style-src": [SELF, "https://cdnjs.cloudflare.com"],
        "font-src": [SELF, "https://cdnjs.cloudflare.com"],
        "frame-src": [SELF, "https://cloud.muelthaler.com", "https://www.canva.com"],
        "frame-ancestors": [SELF, "https://cloud.muelthaler.com"],
    },
}
X_FRAME_OPTIONS = "SAMEORIGIN"


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

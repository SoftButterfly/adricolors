# -*- encoding: utf-8 -*-
import os
import json


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Directory Tree
"""
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.getenv('ADRICOLORS_STATIC_ROOT', os.path.join(BASE_DIR, "static"))
MEDIA_ROOT = os.getenv('ADRICOLORS_MEDIA_ROOT', os.path.join(BASE_DIR, "media"))


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Administrators
"""
ADMINS = (
    ("Martin Josemaria", "martin.vuelta@gmail.com"),
)


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Security
"""

SECRET_KEY = os.getenv("ADRICOLORS_SECRET_KEY", "$Up#r*$#CR#T*k#i")

DEBUG = json.loads(os.getenv("ADRICOLORS_DEBUG_SITE", "true"))

ALLOWED_HOSTS = os.getenv("ADRICOLORS_TEMPLATE_DEBUG", "*").split(":")

SECURE_PROXY_SSL_HEADER = ("ADRICOLORS_HTTP_X_FORWARDED_PROTO", "https")


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Applications
"""
INSTALLED_APPS = [
    # Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Wagtail
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    # Other Third Party
    'captcha',
    'compressor',
    'modelcluster',
    'overextends',
    'rest_framework',
    'taggit',

    # Own
    'home',
    'search',
    'store',
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Middlewares
"""
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Wagtail
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Configuration of URL mapping
"""
STATIC_URL = os.getenv("ADRICOLORS_STATIC_URL", "/static/")
MEDIA_URL = os.getenv("ADRICOLORS_MEDIA_URL", "/media/")
ROOT_URLCONF = 'adricolors.urls'


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Tempaltes
"""
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': ['overextends.templatetags.overextends_tags'],
            'debug': json.loads(os.getenv("ADRICOLORS_DEBUG_TEMPLATES", "true")),
        },
    },
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Static files
"""
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # COmpressor
    'compressor.finders.CompressorFinder',
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Aplicacionde WSGI
"""
WSGI_APPLICATION = 'adricolors.wsgi.application'


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Bases de Datos
"""
DATABASES = {
    'default': {
        "ENGINE": os.getenv("ADRICOLORS_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("ADRICOLORS_DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.getenv("ADRICOLORS_DB_USER", ""),
        "PASSWORD": os.getenv("ADRICOLORS_DB_PASSWORD", ""),
        "HOST": os.getenv("ADRICOLORS_DB_HOST", ""),
        "PORT": os.getenv("ADRICOLORS_DB_PORT", ""),
    }
}


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Password validation
"""
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


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Internacionalization and localization
"""
LANGUAGE_CODE = 'es-es'
TIME_ZONE = os.getenv("ADRICOLORS_TIME_ZONE", "America/Lima")
USE_I18N = True
USE_L10N = True
USE_TZ = True


""" * * * * * * * * * * * * * * * * * *
Wagtail Settings
"""
WAGTAIL_SITE_NAME = 'Adricolors'


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Other Settings
"""
# Google Maps
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Google ReCapthcha
RECAPTCHA_PUBLIC_KEY = os.getenv("GOOGLE_RECAPTCHA_PUBLIC_KEY", "")
RECAPTCHA_PRIVATE_KEY = os.getenv("GOOGLE_RECAPTCHA_PRIVATE_KEY", "")
RECAPTCHA_USE_SSL = True
NOCAPTCHA = True

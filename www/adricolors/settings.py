# -*- encoding: utf-8 -*-
import os
import json


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Directory Tree
"""
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.getenv("STATIC_ROOT", os.path.join(BASE_DIR, "static"))
MEDIA_ROOT = os.getenv("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Administrators
"""
ADMINS = (
    ("SoftButterfly Developer Team", "dev@softbutterfly.space"),
    ("Adricolors Systems Supervisor", "sysadmin@adricolors.com"),
)


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Security
"""
SECRET_KEY = os.getenv("SECRET_KEY", "$Up#r*$#CR#T*k#i")
DEBUG = json.loads(os.getenv("DEBUG_SITE", "true"))
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(":")


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Sessions
"""
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Mailing
"""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "localhost")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "development")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "Tester <tester@development.server>")
EMAIL_SUBJECT_PREFIX = os.getenv("EMAIL_SUBJECT_PREFIX", "[Adricolors] ")
EMAIL_PORT = 25
EMAIL_USE_TLS = True


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Applications
"""
INSTALLED_APPS = [
    # Default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Other Third Party
    "captcha",
    "compressor",
    "modelcluster",
    "overextends",
    "rest_framework",
    "taggit",

    # Own
    "home",
    "search",
    "store",
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Middlewares
"""
MIDDLEWARE_CLASSES = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE_CLASSES = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE_CLASSES

""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Configuration of URL mapping
"""
ROOT_URLCONF = "adricolors.urls"
STATIC_URL = os.getenv("STATIC_URL", "/static/")
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Tempaltes
"""
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "builtins": [
                "overextends.templatetags.overextends_tags",
            ],
            "debug": json.loads(os.getenv("DEBUG_TEMPLATES", "true")),
        },
    },
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Static files
"""
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",

    # Compressor
    "compressor.finders.CompressorFinder",
]


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Aplicacionde WSGI
"""
WSGI_APPLICATION = "adricolors.wsgi.application"


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Bases de Datos
"""
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Password validation
"""
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


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Internacionalization and localization
"""
LANGUAGE_CODE = "es-es"
TIME_ZONE = os.getenv("TIME_ZONE", "America/Lima")
USE_I18N = True
USE_L10N = True
USE_TZ = True


""" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
Other Settings
"""
if DEBUG:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    def show_toolbar(request):
        return True

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
        'RENDER_PANELS': True,
        'INTERNAL_IPS': ['127.0.0.1', '192.168.1.10', '192.168.1.16', '192.168.1.11', ],
        # Toolbar options
        'RESULTS_CACHE_SIZE': 3,
        'SHOW_COLLAPSED': True,
        # Panel options
        'SQL_WARNING_THRESHOLD': 100,   # milliseconds
    }

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

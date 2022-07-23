import os
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool('DEBUG')

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['alsafia-uzb.herokuapp.com','alsafia.uz', 'localhost', '127.0.0.1', '0.0.0.0', '137.184.35.117']

SECRET_KEY = env.str('SECRET_KEY')

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'debug_toolbar',
    'myshop',
    'users'
]

AUTH_USER_MODEL = 'users.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


INTERNAL_IPS = [
    "127.0.0.1",
]


ROOT_URLCONF = 'configs.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'configs.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env.str('POSTGRES_ENGINE'),
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': env.str('POSTGRES_HOST'),
        'PORT': env.str('POSTGRES_PORT'),
    }
}

LOGFILE_PATH = "./"
LOG_LEVEL = env.str('LOG_LEVEL', 'ERROR')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        },
    },

    'handlers': {
        'file': {
            'filename': LOGFILE_PATH + 'alsafia.log',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 20 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'myshop': {
            'level': LOG_LEVEL,
            'handlers': ['file'],
            'propagate': False,
        },
        'django': {
            'level': LOG_LEVEL,
            'handlers': ['file'],
            'propagate': True,
        },
    },
}

MYSERVICE: dict = {
    'redis': {
        'db': env.str('REDIS_DB',0), 
        'host': env.str('REDIS_HOST'),
        'port': env.str('REDIS_PORT'),
        'password': env.str('REDIS_PASS', None),
    },
    'telebot': {
        'base_url': env.str('TELEBOT_URL'),
        'token': env.str('TELEBOT_TOKEN'),
        'chat_id': {
            "chat_id_orders": env.str('TELEBOT_CHAT_ID_ORDERS'),
            "chat_id_warnings": env.str('TELEBOT_CHAT_ID_WARNINGS'),
        }
    },
    'sms_service': {
        'base_url': env.str('SMS_URL'),
        'email': env.str('SMS_EMAIL'),
        'password': env.str('SMS_PASSWORD'),
        'group': env.str('SMS_GROUP'),
        'callback_url': env.str('SMS_CALLBACK_URL'),
    }
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env.str('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CACHE_TTL = 60 * 10

AUTH_PASSWORD_VALIDATORS = []

USE_TZ = True
USE_I18N = True
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR.joinpath('static'))
STATICFILES_DIRS = []

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cors settings
CORS_ORIGIN_ALLOW_ALL = True

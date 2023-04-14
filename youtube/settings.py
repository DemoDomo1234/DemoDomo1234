from pathlib import Path
import os
from neomodel import config, db


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-u$bb^gu-q-l7wiw_o7t-b5b)m9i$3=*_2*(rq5ilpfc8cqkj9s'
DEBUG = True
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'coments.apps.ComentsConfig',
    'list.apps.ListConfig',
    'story.apps.StoryConfig',
    'short.apps.ShortConfig',
    'post.apps.PostConfig',
    'chat.apps.ChatConfig',
    
    'taggit',
    'django_social_share',
    'django_neomodel',
    'django_celery_beat',
    'channels',
    'django_elasticsearch_dsl'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'youtube.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR , 'templates'],
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


WSGI_APPLICATION = 'youtube.wsgi.application'
ASGI_APPLICATION = 'youtube.asgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'youtubesql',
        'USER': 'postgres',
        'PASSWORD': 'demodomo',
        'HOST': 'localhost',
        'PORT': 5432 
    }
    }


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}


SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
CACHE_TTL = 60 * 15


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
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = 'accounts.User'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'demodomone@gmail.com'
DEFAULT_FORM_EMAIL = 'demodomone@gmail.com'
EMAIL_HOST_PASSWORD = 'jjbkvvclqseeixhx'


LOGIN_REDIRECT_URL = 'blog:BlogList'


INTERNAL_IPS = [
   '127.0.0.1',
]


NEOMODEL_NEO4J_BOLT_URL = 'bolt://neo4j:demodomo@localhost:7687'
NEOMODEL_SIGNALS = True
NEOMODEL_FORCE_TIMEZONE = False
NEOMODEL_MAX_CONNECTION_POOL_SIZE = 50


ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:9200'
    },
}


config.DATABASE_URL = 'bolt://neo4j:demodomo@localhost:7687'
db.set_connection('bolt://neo4j:demodomo@localhost:7687')


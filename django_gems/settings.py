import os
from pathlib import Path
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', None)

DEBUG = bool(int(os.getenv('DEBUG')))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(' ')
CSRF_TRUSTED_ORIGINS = [f'http://{x}:80' for x in os.getenv('ALLOWED_HOSTS', '').split(' ')]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_countries',
    'django_gems.user_account.apps.UserAccountConfig',
    'django_gems.common',
    'django_gems.inventory',
    'django_gems.jewelry',
    'django_gems.order',
    'django_gems.user_profile',
    'django_gems.shopping_cart',
    'django_gems.wishlist',

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

ROOT_URLCONF = 'django_gems.urls'

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

WSGI_APPLICATION = 'django_gems.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('DB_NAME'),
        "PASSWORD": os.getenv('DB_PASSWORD'),
        "USER": os.getenv('DB_USER'),
        "HOST": os.getenv('DB_HOST'),
        "PORT": os.getenv('DB_PORT'),
    }
}

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

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static_files',
)

STATIC_ROOT = os.getenv('STATIC_ROOT')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('index_page')
LOGOUT_REDIRECT_URL = reverse_lazy('login_or_register_user')
LOGIN_URL = reverse_lazy('login_or_register_user')

AUTH_USER_MODEL = 'user_account.AccountUser'

COUNTRIES_COMMON_NAMES = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = bool(int(os.getenv('EMAIL_USE_TLS')))
EMAIL_USE_SSL = bool(int(os.getenv('EMAIL_USE_SSL')))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL ')
SERVER_EMAIL = os.getenv('SERVER_EMAIL')




# import os
# from datetime import timedelta
# from pathlib import Path
# from django.urls import reverse_lazy
#
# SESSION_ENGINE = 'session_backends.session_backend'
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# SECRET_KEY = "django-insecure-#&s8j5cg)q%3cnr+sw^2h@0s%$d6o3wlpd1=ed9b1_dpos-$*_"
#
# DEBUG = True
#
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.static',
#
#     'django_celery_beat',
#     'django_countries',
#
#     'django_gems.user_account.apps.UserAccountConfig',
#     'django_gems.common',
#     'django_gems.inventory',
#     'django_gems.jewelry',
#     'django_gems.order',
#     'django_gems.user_profile',
#     'django_gems.shopping_cart',
#     'django_gems.wishlist',
# ]
#
# MIDDLEWARE = [
#     # 'django_gems.middlewares.middlewares.measure_execution_time_middleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'django_gems.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'django_gems.wsgi.application'
#
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "django_gems_db",
#         "PASSWORD": "S@3ana3a",
#         "USER": "postgres",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     }
# }
#
# SESSION_COOKIE_AGE = 3600
# SESSION_SAVE_EVERY_REQUEST = True
#
# # CACHES = {
# #     'default': {
# #         'BACKEND':
# #             'django.core.cache.backends.redis.RedisCache',
# #         'LOCATION':
# #             'redis://127.0.0.1:6379',
# #     },
# # }
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_TZ = True
#
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     BASE_DIR / 'static',
# )
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# LOGIN_REDIRECT_URL = reverse_lazy('index_page')
# LOGOUT_REDIRECT_URL = reverse_lazy('login_or_register_user')
# LOGIN_URL = reverse_lazy('login_or_register_user')
#
# AUTH_USER_MODEL = 'user_account.AccountUser'
#
# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE
#
# COUNTRIES_COMMON_NAMES = False
#
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_HOST_USER = 'djangogems@gmail.com'
# EMAIL_HOST_PASSWORD = 'yuyr nnkd kkkr pkzh'
# DEFAULT_FROM_EMAIL = 'djangogems@gmail.com'
# SERVER_EMAIL = 'djangogems@gmail.com'

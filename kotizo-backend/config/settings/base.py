from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'django_celery_beat',
    'django_celery_results',
    'cloudinary',
    'cloudinary_storage',
    'apps.users',
    'apps.cotisations',
    'apps.paiements',
    'apps.notifications',
    'apps.agent_ia',
    'apps.admin_panel',
    'apps.core',
    'apps.logs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Lome'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
}

CELERY_TIMEZONE = 'Africa/Lome'
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

PAYDUNYA_MASTER_KEY = config('PAYDUNYA_MASTER_KEY')
PAYDUNYA_PRIVATE_KEY = config('PAYDUNYA_PRIVATE_KEY')
PAYDUNYA_TOKEN = config('PAYDUNYA_TOKEN')
PAYDUNYA_MODE = config('PAYDUNYA_MODE', default='test')

EVOLUTION_API_URL = config('EVOLUTION_API_URL', default='http://localhost:8080')
EVOLUTION_API_KEY = config('EVOLUTION_API_KEY')
EVOLUTION_INSTANCE = config('EVOLUTION_INSTANCE', default='kotizo')

GEMINI_API_KEY = config('GEMINI_API_KEY')

GMAIL_USER = config('GMAIL_USER')
GMAIL_PASSWORD = config('GMAIL_PASSWORD')
BREVO_API_KEY = config('BREVO_API_KEY')
MAILJET_API_KEY = config('MAILJET_API_KEY')
MAILJET_SECRET_KEY = config('MAILJET_SECRET_KEY')
RESEND_API_KEY = config('RESEND_API_KEY')

WA_DAILY_LIMITS = {
    'warmup_day_1_10': 20,
    'warmup_day_11_30': 100,
    'normal': 99999,
}

IA_DAILY_LIMITS = {
    'basic': 3,
    'verified': 25,
    'business': 99999,
}

COTISATION_DAILY_LIMITS = {
    'basic': 5,
    'verified': 20,
    'business': 99999,
}

TOKEN_EXPIRY_MINUTES = 5
TOKEN_MAX_ATTEMPTS = 3
TOKEN_BLOCK_HOURS = 12
UNVERIFIED_ACCOUNT_DELETE_HOURS = 48
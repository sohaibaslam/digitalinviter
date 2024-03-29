from digitalinviter.settings.common import *


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = os.environ.get('STATIC_URL')

LOGIN_REDIRECT_URL = "https://digitalinviter.com/login"

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'digital-inviter-data/static')

SITE_ID = 4

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['public_profile', 'user_photos'],
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = os.environ['GS_BUCKET_NAME']

# GCP bucket_key.json set by venv
# os.environ['GOOGLE_APPLICATION_CREDENTIALS']

GS_DEFAULT_ACL = 'publicRead'
GS_FILE_OVERWRITE = False

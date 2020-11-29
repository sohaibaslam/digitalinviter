from digitalinviter.settings.common import *


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'NAME': os.environ.get('DB_NAME', 'digitalinviterdb'),
        'USER': os.environ.get('DB_USER', 'digitalinviter'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'digitalinviter'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = os.environ.get('STATIC_URL', '/static/')

LOGIN_REDIRECT_URL = "https://digitalinviter.com/login"

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'digital-inviter-data/static')

SITE_ID = 4

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['public_profile', 'user_photos'],
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'digitalinviter2'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/digitalinviter/digitalinviter-backend/bucketkey/bucket_key.json'
GS_DEFAULT_ACL = 'publicRead'
GS_FILE_OVERWRITE = False

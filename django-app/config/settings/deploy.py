from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy['aws']['access_key_id']
AWS_SECRET_ACCESS_KEY = config_secret_deploy['aws']['secret_access_key']
AWS_STORAGE_BUCKET_NAME = config_secret_deploy['aws']['s3_bucket_name']
AWS_S3_REGION = config_secret_deploy['aws']['s3_region_name']
S3_USE_SIGV4 = True

# AWS_S3_SIGNATURE_VERSION = config_secret_deploy['aws']['s3_signature_version']

# Sotrage settings
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# Static URLs
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
# media custom
# MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

# 배포모드니까 DEBUG는 False
DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = config_secret_deploy['django']['databases']

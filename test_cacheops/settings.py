"""
Django settings for test_cacheops project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2k^oxk+^#61nh^z5bkr==5qgu90&yat7wtfamb5cx-s#zpbsyg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'cacheops',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'problematic',
    'corsheaders',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test_cacheops.urls'

WSGI_APPLICATION = 'test_cacheops.wsgi.application'


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'transaction_hooks.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'your_db',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {},
        'STORAGE_ENGINE': 'INNODB',
        'CONN_MAX_AGE': 600,
    }
}
########## END DATABASE CONFIGURATION

########## SOUTH CONFIGURATION
SOUTH_TESTS_MIGRATE = False
SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.mysql',
}
########## END SOUTH CONFIGURATION

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

########## CACHEOPS CONFIGURATION
CACHEOPS_DEFAULTS = {
    'timeout': 60 * 60 * 24  # 24 hours
}

CACHEOPS = {
    'problematic.*': {'ops': 'all'},

    ### THIRD PARTY APPS ###
    'auth.*': {'ops': 'all'},
    'sites.*': {'ops': 'all'},
}

CACHEOPS_REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 1,
    'socket_timeout': 5,
}
CACHEOPS_DEGRADE_ON_FAILURE = False
CACHEOPS_FAKE = False
########## END CACHEOPS CONFIGURATION

########## CORS CONFIGURATION
# See: https://github.com/ottoyiu/django-cors-headers/
CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'cache-control',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)
CORS_ORIGIN_WHITELIST = []
CORS_ORIGIN_ALLOW_ALL = False
########## END CORS CONFIGURATION
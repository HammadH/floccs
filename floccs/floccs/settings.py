"""
Django settings for floccs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import django.conf.global_settings as DEFAULT_SETTINGS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&sxd@h7s=^l&(zs9)p(zaj@=(6h)8@%xc8_@_3e0z%sffj8f!c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

LOGIN_URL = '/'
LOGOUT_URL = "/"
LOGIN_REDIRECT_URL = '/home/'
LOGIN_ERROR_URL = '/login-error/'


ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'CustomUser.User'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'south',
    'taggit',
    'debug_toolbar',
    'social_auth',
    'CustomUser',
    'Profile',
    'Projects',
    'Notifications',
    'Message',

    
)


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    
    'social_auth.context_processors.social_auth_by_type_backends',
    ) 

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH =  225
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 225
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 225
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 225

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'


SOCIAL_AUTH_ENABLED_BACKENDS = ('google','twitter','facebook')
SOCIAL_AUTH_USER_MODEL = 'CustomUser.User'

GOOGLE_OAUTH2_CLIENT_ID = '119234541690.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = 'SuFiiy68iqu-GZ5zvITKYdbD'

TWITTER_CONSUMER_KEY         = '3p2S8oDcoyBb7ndT9F6wJw'
TWITTER_CONSUMER_SECRET      = 'A4Of0OFCJnI32ULhcrEVMeYCChqtL2PmOwZKI5JLw'

FACEBOOK_APP_ID              = '584295751657017'
FACEBOOK_API_SECRET          = '48728289f1737eb56a1a98ce969aaee8'
FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_location']

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'floccs.urls'

WSGI_APPLICATION = 'floccs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'floccs_db',
        'USER': 'hammad',
        'PASSWORD': 'quakeroats',
        'HOST': ''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

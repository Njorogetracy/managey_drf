"""
Django settings for managey_drf project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
import re

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

REST_FRAMEWORK = {
    # use session authentication in Dev & JSON Web Token auth in Prod
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}

# render JSON in PROD
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

# enable token authentication
REST_USE_JWT = True
# make sure to send over HTTPS only
JWT_AUTH_SECURE = True
# access token
JWT_AUTH_COOKIE = 'my-app-auth'
# refresh token
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
# allow front end and back end deployed to different platforms
JWT_AUTH_SAMESITE = 'None'

# override default serializer
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'managey_drf.serializers.CurrentUserSerializer'
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = 'DEV' in os.environ
DEBUG = False

CSRF_TRUSTED_ORIGINS = [
    'https://managey-a1b31600d931.herokuapp.com',
    'https://manageydrf-8a469d59154b.herokuapp.com',
    'https://localhost:3000',
    'https://*.127.0.0.1',
    'https://8000-njorogetracy-manageydrf-fouja6zojup.ws-eu117.gitpod.io',
    'https://3000-njorogetracy-managey-hppr9jkculs.ws-eu117.gitpod.io',
    'https://8000-njorogetracy-manageydrf-qt48gzd5j16.ws-eu117.gitpod.io',
    'https://3000-njorogetracy-managey-1oyr39h082d.ws-eu117.gitpod.io',
    'https://8080-njorogetracy-manageydrf-6yzu06ox9vm.ws-eu117.gitpod.io',
    'https://8000-njorogetracy-manageydrf-zmg7lvoxv21.ws.codeinstitute-ide.net',
    'https://8000-njorogetracy-manageydrf-yg2uhgywowr.ws-eu117.gitpod.io',
    'https://3000-njorogetracy-managey-uqidzch6dq8.ws-eu117.gitpod.io',
    'https://8000-njorogetracy-manageydrf-y4gopnnwl7d.ws-eu117.gitpod.io'
]

ALLOWED_HOSTS = [
    os.environ.get('ALLOWED_HOST'),
    'manageydrf-8a469d59154b.herokuapp.com',
    'managey-a1b31600d931.herokuapp.com',
    'localhost',
    '8000-njorogetracy-manageydrf-zmg7lvoxv21.ws.codeinstitute-ide.net',
    '8000-njorogetracy-manageydrf-fouja6zojup.ws-eu117.gitpod.io',
    '8000-njorogetracy-manageydrf-qt48gzd5j16.ws-eu117.gitpod.io',
    '8000-njorogetracy-manageydrf-6yzu06ox9vm.ws-eu117.gitpod.io',
    '3000-njorogetracy-managey-1oyr39h082d.ws-eu117.gitpod.io',
    '8080-njorogetracy-manageydrf-6yzu06ox9vm.ws-eu117.gitpod.io',
    '8000-njorogetracy-manageydrf-yg2uhgywowr.ws-eu117.gitpod.io',
    '3000-njorogetracy-managey-uqidzch6dq8.ws-eu117.gitpod.io',
    '8000-njorogetracy-manageydrf-y4gopnnwl7d.ws-eu117.gitpod.io'
]


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
                        'https://managey-a1b31600d931.herokuapp.com',
                        'https://manageydrf-8a469d59154b.herokuapp.com',
                        'https://3000-njorogetracy-managey-47om2pk1bb3.ws-eu117.gitpod.io',
                        'https://3000-njorogetracy-managey-g2u276z7yhs.ws.codeinstitute-ide.net',
                        'https://3000-njorogetracy-managey-hppr9jkculs.ws-eu117.gitpod.io',
                        'https://8000-njorogetracy-manageydrf-fouja6zojup.ws-eu117.gitpod.io',
                        'https://8000-njorogetracy-manageydrf-qt48gzd5j16.ws-eu117.gitpod.io',
                        'https://3000-njorogetracy-managey-1oyr39h082d.ws-eu117.gitpod.io',
                        'https://8080-njorogetracy-manageydrf-6yzu06ox9vm.ws-eu117.gitpod.io',
                        'https://3000-njorogetracy-managey-uqidzch6dq8.ws-eu117.gitpod.io'
                        ]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',

    'profiles',
    'tasks',
    'comments',
]

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(
        r'^.+-',
        os.environ.get('CLIENT_ORIGIN_DEV', ''),
        re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'managey_drf.urls'

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

WSGI_APPLICATION = 'managey_drf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

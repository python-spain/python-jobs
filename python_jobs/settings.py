"""
Django settings for python_jobs project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
from os.path import abspath, basename, dirname, join, normpath

from configurations import Configuration, values


class Base(Configuration):
    # Build paths inside the project like this: join(BASE_DIR, ...)
    BASE_DIR = dirname(dirname(abspath(__file__)))

    ########## PATH CONFIGURATION
    # Absolute filesystem path to the Django project directory:
    DJANGO_ROOT = dirname(dirname(abspath(__file__)))

    # Absolute filesystem path to the top-level project folder:
    SITE_ROOT = dirname(DJANGO_ROOT)

    # Site name:
    SITE_NAME = basename(DJANGO_ROOT)

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '%*2$we$d_km*#@z*s^rvjum2e!m$(+84k6oqt@ls$d-xbg5hlc'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'cities_light',
        'jobs',
        'crispy_forms',
        'django_rq'
    ]

    MIDDLEWARE_CLASSES = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'python_jobs.urls'

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

    WSGI_APPLICATION = 'python_jobs.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.9/ref/settings/#databases
    DATABASES = values.DatabaseURLValue("postgres://localhost/pythonjobs")

    # Password validation
    # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


    # Internationalization
    # https://docs.djangoproject.com/en/1.9/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    CITIES_LIGHT_TRANSLATION_LANGUAGES = ['es', 'en', 'abbr']
    CITIES_LIGHT_INCLUDE_COUNTRIES = ['ES', ]

    RQ_QUEUES = {
        'default': {
            'HOST': 'localhost',
            'PORT': 6379,
            'DB': 0,
            'PASSWORD': 'some-password',
            'DEFAULT_TIMEOUT': 360,
        },
    }

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        normpath(join(SITE_ROOT, 'static')),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


class Prod(Base):
    DEBUG = False
    DATABASES = values.DatabaseURLValue()
    ALLOWED_HOSTS = ['*']

    RQ_QUEUES = {
        'default': {
            'URL': os.getenv('REDIS_URL', ''),  # If you're on Dokku
            'DEFAULT_TIMEOUT': 500,
        }
    }

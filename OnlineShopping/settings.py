# from pathlib import Path
# from django.conf import settings
import os
import django_heroku
 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# os.path.join(os.path.dirname(os.path.dirname(__file__)),'media/documents/GDRAT.xls')
# base_dir =settings.MEDIA_ROOT
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = Path(__file__).resolve().parent.parent


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

 
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ujsx7y@d*q^b)ta6v6=v!3)ut4e0-zsg6xtlfp3qirfp5$#(3q'
 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
 
CSRF_COOKIE_SECURE = True
 
# security.W012
SESSION_COOKIE_SECURE = True
 
# security.W008
SECURE_SSL_REDIRECT = True
 
# security.W004
SECURE_HSTS_SECONDS = 31536000 # One year in seconds
 
# Another security settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
 
 
ALLOWED_HOSTS = ['localhost',
  '127.0.0.1','michronia.herokuapp.com ','*']

 
 
 
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'django.contrib.humanize',
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
 
ROOT_URLCONF = 'OnlineShopping.urls'
 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["shop/templates"],
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
 
WSGI_APPLICATION = 'OnlineShopping.wsgi.application'
 
 
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 
 
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
 
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
# https://docs.djangoproject.com/en/3.1/topics/i18n/
 
LANGUAGE_CODE = 'en-us'
 
TIME_ZONE = 'UTC'
 
USE_I18N = True
 
USE_L10N = True
 
USE_TZ = True
 
 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
 
 
 
MEDIA_ROOT = os.path.join(BASE_DIR, '/static')
MEDIA_URL = '/media/'
 
 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "/static")
# ]
 
 
 
 



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


django_heroku.settings(locals())
 
 



































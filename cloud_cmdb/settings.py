"""
Django settings for cloud_cmdb project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6hg&kh1!z&_s6+i&8dw#q=1g&fz%d=e-mv#29bi&ncb-8(y11&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloud.apps.CloudConfig',
    'host',
    'cloud_public'
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

ROOT_URLCONF = 'cloud_cmdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'cloud_cmdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('MYSQL_HOST', None),
        'NAME': os.environ.get('NYSQL_DB', None),
        'USER': os.environ.get('MYSQL_USER', None),
        'PASSWORD': os.environ.get('MYSQL_PASS', None),
        'PORT': int(os.environ.get('MYSQL_PORT', 3306)),
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

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 存放Log的目录
LOGGING_DIR = os.path.join(BASE_DIR, 'log')

LOGGING = {
    'version': 1,
     'disable_existing_loggers': True,
     'formatters': {
         'simple': {
             'format': '[%(asctime)s] %(levelname)s : %(message)s'
         },
         'verbose': {
             'format': '[%(asctime)s] %(levelname)s %(module)s %(process)d %(thread)d : %(message)s'
         },
         'standard': {
             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
         },
     },
    # handlers：用来定义具体处理日志的方式，可以定义多种，"default"就是默认方式，"console"就是打印到控制台方式。file是写入到文件的方式，注意使用的class不同
     'handlers': {
         'mail_admins':{
             'level': 'ERROR',
             'class': 'django.utils.log.AdminEmailHandler',
             'include_html': True,
         },
         'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'run.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'simple',
         },
         # 'request_handler': {
         #     'level': 'DEBUG',
         #     'class': 'logging.handlers.RotatingFileHandler',
         #     'filename': os.path.join(LOGGING_DIR, 'debug_request.log'),
         #     'maxBytes': 1024*1024*5,
         #     'backupCount': 5,
         #     'formatter': 'standard',
         # },
         'console': {
             'level': 'INFO',
             'class': 'logging.StreamHandler',  # 用这'logging.StreamHandler' 日志信息才会输出到console
             # 'filename':os.path.join(LOGGING_DIR,'info_console.log'),
             # 'formatter': 'standard',
             'formatter': 'simple',
         },
     },
    # log记录器，配置之后就会对应的输出日志
     'loggers': {
         'django': {
             # 'handlers': ['console', '  ', 'default'],
             'handlers': ['console', 'default'],
             'level': 'INFO',
             'propagate': True,
         },
     },
}

# 'django'是一种类型的日志
import logging
logger = logging.getLogger("django")
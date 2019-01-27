"""
Django settings for aliyun project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'onz1*zmz(5r5-ax28)@@w)5-@x^#789j2$^3pkp_j05$vd^xf_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'MainIndex',
    'SystemSettings',
    'Commodity',
    'Models',
    'security',
    'WorkOrder',
    'customermanager',
    'Base',
]


#   Session通用配置
SESSION_COOKIE_NAME = "sessionid"
# Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = True
# 是否每次请求都保存Session，默认修改之后才保存（默认）

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'aliyun.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
       # 'APP_DIRS': True,
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                 'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'aliyun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',#'sql_server.pyodbc',django_pyodbc',
        'NAME':'aliyun',
        'HOST':'39.108.107.126',
        #'HOST':'localhost',
        'PORT':'3306',
        'USER':'user',
        'PASSWORD':'user',
        # 'USER':'root',
        # 'PASSWORD':'1234',
        'OPTIONS': {
           'init_command': 'SET sql_mode=STRICT_TRANS_TABLES',
        },
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = False
USE_L10N = False #为True会使format不生效
DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i:s'
###auto_now 用update不会更新
# USE_TZ = True
USE_TZ = False
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# 使用时的前缀 href=/static/xxx.css,就会在commonstatic下找这个文件
STATIC_URL = '/static/'
#STATIC_XXX配置项用来管理静态文件。它们通过manage.py collectstatic命令汇集到settings.STATIC_ROOT目录，并通过settings.STATIC_URL指定的路径访问。
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "commonstatic/"),#一定要加  逗号！
)#公共静态文件夹名
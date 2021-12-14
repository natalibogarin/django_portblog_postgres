from .base import *


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portblog',
        'USER': 'roottest',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
        
    }
}

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL ='/'
LOGOUT_REDIRECT_URL = '/'
import os
from .settings import *
from .settings import BASE_DIR

#adresy do backendu 
ALLOWED_HOSTS= [os.environ['WEBSITE_HOSTNAME']]

CSRF_TRUSTED_ORIGINS= ['https://' + os.environ['WEBSITE_HOSTNAME']]

DEBUG= False





#POZNIEJ USTAWIE NA AZURE ZMIENNA Z TYM SECRET KEY
SECRET_KEY= os.environ['MY_SECRET_KEY']

MIDDLEWARE= [
     "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

    'django.middleware.security.SecurityMiddleware',


    'whitenoise.middleware.WhiteNoiseMiddleware',


    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#CORS_ALLOWED_ORIGINS= [
#    ''
#]

STORAGES= {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },

    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CONNECTION= os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNECTION_STR= {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}
DATABASES = {
    #pdomienic na dane z Azure
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONNECTION_STR['dbname'],
        "HOST": CONNECTION_STR['host'],
        "USER": CONNECTION_STR['user'],
        "PASSWORD": CONNECTION_STR['password'],  
    }
}

#STATIC_ROOT= BASE_DIR/'staticfiles'


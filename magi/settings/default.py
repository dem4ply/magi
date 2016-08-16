# vim: set fileencoding=utf-8 :
import os
from django.utils.translation import ugettext_lazy as _
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath( __file__ ) ) )

SECRET_KEY = '163#*qyk5fk3v1hmq=jmteiy%_9=pmc8t4v3ms!iebyv!)_7if'

DEBUG = True

ALLOWED_HOSTS = [ '*' ]

from .email import default

from .installed_apps.default import *
from .middleware_classes.default import *
from .rest_framework.default import *
from .cors.default import *
from .database.default import DATABASES
from .logger.default import LOGGING
from .elasticsearch.default import connections

ROOT_URLCONF = 'magi.urls'

WSGI_APPLICATION = 'magi.wsgi.application'

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ( 'es', _( 'Español' ) ),
    ( 'en', _( 'Ingles') ),
)
LOCALE_PATHS = ( os.path.join( BASE_DIR, 'locale' ), )

STATIC_URL = '/static/'

DEFAULT_CHARSET = 'utf-8'

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

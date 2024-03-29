from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-esii%uzn3r*v^7x#j+63t6_dbd_-#a#_i5$+xogr1k1g%71c@l"


DEBUG = True

#ALLOWED_HOSTS = ['3.88.215.98', '44.203.137.249']
ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'bootstrapform',
    
    "apps.core",
    "apps.empresa",
    "apps.funcionarios",
    "apps.departamentos",
    "apps.documentos",
    "apps.hora_extra",
    "apps.app_antigo",
   
   'rest_framework',
   'rest_framework.authtoken',

   'django_celery_results',
   'django_celery_beat',
   

]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "Gestao_RH.urls"


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]


WSGI_APPLICATION = "Gestao_RH.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },

    "antigo": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db_antigo.sqlite3",
    },
    
    'postgres': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'gestao_rh_postgre',

        'USER': 'user_gestao_rh',

        'PASSWORD': 'gestao_rh123',

        'HOST': 'localhost',

        'PORT': '',

    }
}

#configuação para que o admin do django reconheça banco de dados antigo
DATABASE_ROUTERS = ['Gestao_RH.DbRouters.DBRoutes']

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "pt-br"

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True



STATIC_URL = "/static/"

if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_URL = 'login'             
LOGIN_REDIRECT_URL = 'home'     
LOGOUT_REDIRECT_URL = 'login'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'

CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = 'contato@devacademy.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'contato@devacademy.com'
EMAIL_HOST_PASSWORD = 'ztyuodophslszhms'
EMAIL_PORT = 587

CONTACT_EMAIL = 'contato@devacademy.com'


#CONFIGURAÇÃO PARA TRADUÇÕES DE PAGINAS COM DJANGO
LANGUAGES = (
    ('en', _('English')),
    ('pt', _('Portugues')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
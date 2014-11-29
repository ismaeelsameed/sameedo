from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'aj^)2$p-cnp68gj%@s&g9zsg9)l$e!23t_rgu)nvsk52mv)*ds'

# 3rd-party apps tracking IDs.
# INTERCOM_APP_ID = None
# GOOGLE_ANALYTICS_TRACKING_ID = None
# ADDTHIS_PUBLISHER_ID = None

EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'test'
EMAIL_HOST_PASSWORD = 'test'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# ADMINS = (
#     ('Local Admin', 'admin@glucosetracker.net'),
# )

# MANAGERS = ADMINS

# CONTACTS = {
#     'support_email': 'support@glucosetracker.net',
#     'admin_email': 'admin@glucosetracker.net',
#     'info_email': 'info@glucosetracker.net',
# }

# For 'subscribers' app
# SEND_SUBSCRIBERS_EMAIL_CONFIRMATION = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'sameedo',
#         'USER': 'sameedo',
#         'PASSWORD': '0788060672',
#         'HOST': os.environ.get('POSTGRESQL_HOST', 'localhost'),
#         'PORT': '',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_ROOT + '/' + "sameedo.db",
    }
}

# Django-debug-toolbar config
# INSTALLED_APPS += ('debug_toolbar',)
# INTERNAL_IPS = (
#     '127.0.0.1',
#     '192.168.33.1',
#     '172.17.42.1',
# )
# MIDDLEWARE_CLASSES += \
#     ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'SHOW_TEMPLATE_CONTEXT': True,
#     'HIDE_DJANGO_SQL': False,
# }
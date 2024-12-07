
SECRET_KEY = '###'

DEBUG = False

ALLOWED_HOSTS = ['###']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'algo_lib',
        'USER': 'algo_lib',
        'PASSWORD': '###',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'charset': '###',
            'sql_mode': 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION',
        },
    },
}

LANGUAGE_CODE = 'en-us'
DEFAULT_USER_TIME_ZONE = 'Asia/Seoul'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thanhdanhbka@gmail.com'
EMAIL_HOST_PASSWORD = '###'
EMAIL_PORT = ###


STATIC_ROOT = '/static'

SITE_NAME = 'Algo-lib'
SITE_LONG_NAME = 'Algo-lib'
SITE_ADMIN_EMAIL = 'thanhdanhbka@gmail.com'

BRIDGED_JUDGE_ADDRESS = [('localhost', 9999)]


BAD_MAIL_PROVIDERS = set()

ACE_URL = '//cdnjs.cloudflare.com/ajax/libs/ace/1.2.3/'
JQUERY_JS = '//cdnjs.cloudflare.com/ajax/libs/jquery/2.2.4/jquery.min.js'
SELECT2_JS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/js/select2.min.js'
SELECT2_CSS_URL = '//cdnjs.cloudflare.com/ajax/libs/select2/4.0.3/css/select2.min.css'

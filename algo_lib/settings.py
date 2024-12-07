import datetime
import os

from django.utils.translation import gettext_lazy as _
from django_jinja.builtins import DEFAULT_EXTENSIONS
from jinja2 import select_autoescape

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '###'

DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1
SITE_NAME = 'Algo-lib'
SITE_LONG_NAME = 'Algo-lib'
SITE_ADMIN_EMAIL = ''

MARKDOWN_STYLES = {}
MARKDOWN_DEFAULT_STYLE = {}

MATHOID_URL = False
MATHOID_GZIP = False
MATHOID_MML_CACHE = None
MATHOID_CSS_CACHE = 'default'
MATHOID_DEFAULT_TYPE = 'auto'
MATHOID_MML_CACHE_TTL = 86400
MATHOID_CACHE_ROOT = ''
MATHOID_CACHE_URL = False

TEXOID_GZIP = False
TEXOID_META_CACHE = 'default'
TEXOID_META_CACHE_TTL = 86400

BAD_MAIL_PROVIDERS = ()
BAD_MAIL_PROVIDER_REGEX = ()
NOFOLLOW_EXCLUDED = set()

TERMS_OF_SERVICE_URL = None
DEFAULT_USER_LANGUAGE = 'PY3'

INLINE_JQUERY = True
INLINE_FONTAWESOME = True
JQUERY_JS = '//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'
FONTAWESOME_CSS = '//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css'

INSTALLED_APPS = ()

try:
    import wpadmin
except ImportError:
    pass
else:
    del wpadmin
    INSTALLED_APPS += ('wpadmin',)

    WPADMIN = {
        'admin': {
            'title': 'Admin',
            'menu': {
                'top': 'wpadmin.menu.menus.BasicTopMenu',
                'left': 'wpadmin.menu.custom.CustomModelLeftMenuWithDashboard',
            },
            'custom_menu': [
                {
                    'model': 'judge.Problem',
                    'icon': 'fa-question-circle',
                    'children': [
                        'judge.ProblemGroup',
                        'judge.ProblemType',
                        'judge.License',
                        'judge.ProblemPointsVote',
                    ],
                },
                ('judge.Submission', 'fa-check-square-o'),
                {
                    'model': 'judge.Language',
                    'icon': 'fa-file-code-o',
                    'children': [
                        'judge.Judge',
                    ],
                },
                {
                    'model': 'judge.Contest',
                    'icon': 'fa-bar-chart',
                    'children': [
                        'judge.ContestParticipation',
                        'judge.ContestTag',
                    ],
                },
                ('judge.Ticket', 'fa-bell'),
                {
                    'model': 'auth.User',
                    'icon': 'fa-user',
                    'children': [
                        'judge.Profile',
                        'auth.Group',
                        'registration.RegistrationProfile',
                    ],
                },
                {
                    'model': 'judge.Organization',
                    'icon': 'fa-users',
                    'children': [
                        'judge.OrganizationRequest',
                        'judge.Class',
                    ],
                },
                {
                    'model': 'judge.NavigationBar',
                    'icon': 'fa-bars',
                    'children': [
                        'sites.Site',
                        'redirects.Redirect',
                    ],
                },
                ('judge.BlogPost', 'fa-rss-square'),
                {
                    'model': 'judge.Comment',
                    'icon': 'fa-comment-o',
                    'children': [
                        'judge.CommentLock',
                    ],
                },
                ('flatpages.FlatPage', 'fa-file-text-o'),
                ('judge.MiscConfig', 'fa-question-circle'),
            ],
            'dashboard': {
                'breadcrumbs': True,
            },
        },
    }

INSTALLED_APPS += (
    'django.contrib.admin',
    'judge',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'registration',
    'mptt',
    'reversion',
    'django_social_share',
    'social_django',
    'compressor',
    'django_ace',
    'pagedown',
    'sortedm2m',
    'statici18n',
    'impersonate',
    'django_jinja',
    'martor',
    'adminsortable2',
)

MIDDLEWARE = (
    'judge.middleware.ShortCircuitMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'judge.middleware.APIMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'judge.middleware.MiscConfigMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'judge.user_log.LogUserAccessMiddleware',
    'judge.timezone.TimezoneMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'judge.middleware.ContestMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'judge.social_auth.SocialAuthExceptionMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

IMPERSONATE_REQUIRE_SUPERUSER = True
IMPERSONATE_DISABLE_LOGGING = True

ACCOUNT_ACTIVATION_DAYS = 7

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'judge.utils.pwned.PwnedPasswordsValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SILENCED_SYSTEM_CHECKS = ['urls.W002', 'fields.W342']

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'match_extension': ('.html', '.txt'),
            'match_regex': '^(?!admin/)',
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'judge.template_context.comet_location',
                'judge.template_context.get_resource',
                'judge.template_context.general_info',
                'judge.template_context.site',
                'judge.template_context.site_name',
                'judge.template_context.site_theme',
                'judge.template_context.misc_config',
                'judge.template_context.math_setting',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'autoescape': select_autoescape(['html', 'xml']),
            'trim_blocks': True,
            'lstrip_blocks': True,
            'translation_engine': 'judge.utils.safe_translations',
            'extensions': DEFAULT_EXTENSIONS + [
                'compressor.contrib.jinja2ext.CompressorExtension',
                'judge.jinja2.spaceless.SpacelessExtension',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('ca', _('Catalan')),
    ('de', _('German')),
    ('el', _('Greek')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('hr', _('Croatian')),
    ('hu', _('Hungarian')),
    ('ja', _('Japanese')),
    ('kk', _('Kazakh')),
    ('ko', _('Korean')),
    ('pt', _('Brazilian Portuguese')),
    ('ro', _('Romanian')),
    ('ru', _('Russian')),
    ('sr-latn', _('Serbian (Latin)')),
    ('tr', _('Turkish')),
    ('vi', _('Vietnamese')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese')),
]

BLEACH_USER_SAFE_TAGS = [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'b', 'i', 'strong', 'em', 'tt', 'del', 'kbd', 's', 'abbr', 'cite', 'mark', 'q', 'samp', 'small',
    'u', 'var', 'wbr', 'dfn', 'ruby', 'rb', 'rp', 'rt', 'rtc', 'sub', 'sup', 'time', 'data',
    'p', 'br', 'pre', 'span', 'div', 'blockquote', 'code', 'hr',
    'ul', 'ol', 'li', 'dd', 'dl', 'dt', 'address', 'section', 'details', 'summary',
    'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td', 'caption', 'colgroup', 'col', 'tfoot',
    'img', 'audio', 'video', 'source',
    'a',
    'style', 'noscript', 'center',
]

BLEACH_USER_SAFE_ATTRS = {
    '*': ['id', 'class', 'style'],
    'img': ['src', 'alt', 'title', 'width', 'height', 'data-src', 'align'],
    'a': ['href', 'alt', 'title'],
    'abbr': ['title'],
    'dfn': ['title'],
    'time': ['datetime'],
    'data': ['value'],
    'td': ['colspan', 'rowspan'],
    'th': ['colspan', 'rowspan'],
    'audio': ['autoplay', 'controls', 'crossorigin', 'muted', 'loop', 'preload', 'src'],
    'video': ['autoplay', 'controls', 'crossorigin', 'height', 'muted', 'loop', 'poster', 'preload', 'src', 'width'],
    'source': ['src', 'srcset', 'type'],
    'li': ['value'],
}

MARKDOWN_STAFF_EDITABLE_STYLE = {
    'safe_mode': False,
    'use_camo': True,
    'texoid': True,
    'math': True,
    'bleach': {
        'tags': BLEACH_USER_SAFE_TAGS,
        'attributes': BLEACH_USER_SAFE_ATTRS,
        'styles': True,
        'mathml': True,
    },
}

MARKDOWN_ADMIN_EDITABLE_STYLE = {
    'safe_mode': False,
    'use_camo': True,
    'texoid': True,
    'math': True,
}

MARKDOWN_DEFAULT_STYLE = {
    'safe_mode': True,
    'nofollow': True,
    'use_camo': True,
    'math': True,
}

MARKDOWN_USER_LARGE_STYLE = {
    'safe_mode': True,
    'nofollow': True,
    'use_camo': True,
    'math': True,
}

MARKDOWN_STYLES = {
    'default': MARKDOWN_DEFAULT_STYLE,
    'comment': MARKDOWN_DEFAULT_STYLE,
    'self-description': MARKDOWN_USER_LARGE_STYLE,
    'problem': MARKDOWN_STAFF_EDITABLE_STYLE,
    'problem-full': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'contest': MARKDOWN_STAFF_EDITABLE_STYLE,
    'flatpage': MARKDOWN_ADMIN_EDITABLE_STYLE,
    'language': MARKDOWN_STAFF_EDITABLE_STYLE,
    'license': MARKDOWN_STAFF_EDITABLE_STYLE,
    'judge': MARKDOWN_STAFF_EDITABLE_STYLE,
    'blog': MARKDOWN_STAFF_EDITABLE_STYLE,
    'solution': MARKDOWN_STAFF_EDITABLE_STYLE,
    'hint': MARKDOWN_STAFF_EDITABLE_STYLE,
    'contest_tag': MARKDOWN_STAFF_EDITABLE_STYLE,
    'organization-about': MARKDOWN_USER_LARGE_STYLE,
    'ticket': MARKDOWN_USER_LARGE_STYLE,
}

MARTOR_ENABLE_CONFIGS = {
    'imgur': 'true',
    'mention': 'true',
    'jquery': 'false',
    'living': 'false',
    'spellcheck': 'false',
    'hljs': 'false',
}
MARTOR_MARKDOWNIFY_URL = '/widgets/preview/default'
MARTOR_SEARCH_USERS_URL = '/widgets/martor/search-user'
MARTOR_UPLOAD_URL = '/widgets/martor/upload-image'
MARTOR_MARKDOWN_BASE_MENTION_URL = '/user/'

MARTOR_UPLOAD_MEDIA_DIR = 'martor'
MARTOR_UPLOAD_SAFE_EXTS = {'.jpg', '.png', '.gif'}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

ENABLE_FTS = False

BRIDGED_JUDGE_ADDRESS = [('localhost', 9999)]
BRIDGED_JUDGE_PROXIES = None
BRIDGED_DJANGO_ADDRESS = [('localhost', 9998)]
BRIDGED_DJANGO_CONNECT = None

EVENT_DAEMON_USE = False
EVENT_DAEMON_POST = 'ws://localhost:9997/'
EVENT_DAEMON_GET = 'ws://localhost:9996/'
EVENT_DAEMON_POLL = '/channels/'
EVENT_DAEMON_SUBMISSION_KEY = '6Sdmkx^%pk@GsifDfXcwX*Y7LRF%RGT8vmFpSxFBT$fwS7trc8raWfN#CSfQuKApx&$B#Gh2L7p%W!Ww'

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
DEFAULT_USER_TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'resources'),
]
STATIC_URL = '/static/'

CACHES = {}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'judge.social_auth.GitHubSecureEmailOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'judge.social_auth.verify_email',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'judge.social_auth.choose_username',
    'social_core.pipeline.user.create_user',
    'judge.social_auth.make_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GITHUB_SECURE_SCOPE = ['user:email']
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_SLUGIFY_USERNAMES = True
SOCIAL_AUTH_SLUGIFY_FUNCTION = 'judge.social_auth.slugify_username'

MOSS_API_KEY = None

CELERY_WORKER_HIJACK_ROOT_LOGGER = False

WEBAUTHN_RP_ID = None

try:
    with open(os.path.join(os.path.dirname(__file__), 'local_settings.py')) as f:
        exec(f.read(), globals())
except IOError:
    pass



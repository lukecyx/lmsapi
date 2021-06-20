from .base import *
from .get_secrets import get_secret as secret


DEBUG = True
IS_LOCAL = True
IS_TEST = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "OPTIONS": {"options": "-c search_path=lms,public"},
        "NAME": "lmslocal",
        "USER": "luke",
        "PASSWORD": secret("DB_PASSWORD"),
        "HOST": "localhost",
        "TEST": {"NAME": "lmslocal_test"},
    },
}

LOGGING = {
    "version": 1,
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
            "handlers": ["console"],
        }
    },
}

ALLOWED_HOSTS = secret("ALLOWED_HOSTS")
INSTALLED_APPS += ["apps.test_utils"]  # noqa: F405

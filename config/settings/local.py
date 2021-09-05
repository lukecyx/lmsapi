import os

from .base import *


DEBUG = os.environ.get("DEBUG", default=0)
IS_LOCAL = True
IS_TEST = False

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "DB_PORT": os.environ.get("DB_PORT"),
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

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
INSTALLED_APPS += ["apps.test_utils"]  # noqa: F405

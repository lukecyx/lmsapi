from .base import *
from .get_secrets import get_secret as secret

DEBUG = False
IS_LOCAL = False
# IS_LOCAL = True
IS_TEST = True

# TODO: Set up QA/Test db. Not essential right now.
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

ALLOWED_HOSTS = secret("ALLOWED_HOSTS")

INSTALLED_APPS += ["apps.test_utils"]  # noqa: F40

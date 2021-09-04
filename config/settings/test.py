from .base import *

DEBUG = False
IS_LOCAL = False
IS_TEST = True

import os

# TODO: Set up QA/Test db. Not essential right now.

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

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS")

INSTALLED_APPS += ["apps.test_utils"]  # noqa: F40

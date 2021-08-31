from pathlib import Path
from os import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = environ.get("SECRET_KEY")

INSTALLED_APPS = [
    # Defaults.
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Custom.
    "apps.users",
    # Third party.
    "corsheaders",
]


# Ordering of middleware matters.
# See: https://docs.djangoproject.com/en/3.2/topics/http/middleware/#activating-middleware  # noqa: line_too_long
# Custom Middlewares will have a comment above them.
MIDDLEWARE = [
    # Custom.
    "apps.lib.middleware.content_type.ContentTypeMiddleware",
    # Custom.
    "apps.lib.middleware.json_data_loader.JsonDataLoaderMiddleware",
    # Third party.
    "corsheaders.middleware.CorsMiddleware",
    # Default.
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Custom.
    "apps.lib.middleware.api_error.APIErrorMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: line_too_long
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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.joinpath("static")

MEDIA_URL = "/MEDIA/"
MEDIA_ROOT = BASE_DIR.joinpath("media")


ROOT_URLCONF = "config.urls"

API_VERSION = 1

AUTH_USER_MODEL = "users.CustomUser"

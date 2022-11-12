"""
Django settings
"""

import os
from pathlib import Path

# Get the directory manage.py is in
BASE_DIR = Path(__file__).resolve().parent.parent
# Get the directory this file is in (and where all 'local' apps are)
APP_DIR = Path(__file__).resolve().parent

# If it exists, install django-stubs monkeypatching
try:
    import django_stubs_ext

    django_stubs_ext.monkeypatch()
except ImportError:
    pass


def env_bool(env_name: str, default=False) -> bool:
    return os.environ.get(env_name, default=str(default)).lower() in {"1", "t", "true"}


# If DJANGO_DOTENV, load a .env file. Can be useful in dev, don't do this in production
if env_bool("DJANGO_DOTENV"):
    lines = [
        line.split("=", maxsplit=1) for line in (BASE_DIR / ".env").read_text().splitlines()
        if line and not line.startswith('#')
    ]
    for name, value in lines:
        os.environ.setdefault(name.strip(), value)

DEBUG = env_bool("DEBUG")
# we can override this for testing, so that django template coverage can be calculated
TEMPLATE_DEBUG = env_bool("TEMPLATE_DEBUG", default=DEBUG)
# These should definitely always be defined in production deployments
ALLOWED_HOSTS = ["*", ] if DEBUG else [x.strip() for x in os.environ["ALLOWED_HOSTS"].split(",")]
SECRET_KEY = os.environ.get("SECRET_KEY", default="{{ secret_key }}")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    },
}

INSTALLED_APPS = [
    # "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    # "django.contrib.messages",
    # "django.contrib.staticfiles",
    "{{ project_name }}.core",
    "{{ project_name }}.users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{ project_name }}.urls"
ASGI_APPLICATION = "{{ project_name }}.asgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "loaders": [
                ("django.template.loaders.cached.Loader", ["django.template.loaders.app_directories.Loader", ],),
            ],
            "debug": TEMPLATE_DEBUG,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                # "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]

# Rarely needs to be changed for "normal" django projects
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True

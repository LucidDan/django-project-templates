"""
Django application in a single python module.

Probably not suitable for most use cases.
"""

import os
import sys

from django.conf import settings
from django.core.asgi import get_asgi_application
from django.http import HttpResponse
from django.urls import path
from django.utils import html


def index(request):
    name = request.GET.get("name", "world")
    return HttpResponse(f"Hello, {html.escape(name)}")


urlpatterns = [
    path("", index)
]


def application():
    return get_asgi_application()


def main():
    from django.core.management import execute_from_command_line

    settings.configure(
        ALLOWED_HOSTS=["*", ],
        DEBUG=os.environ.get("DEBUG", "").lower() in {"1", "true", "t"},
        ROOT_URLCONF=__name__,
    )

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

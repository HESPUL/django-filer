from django.urls import re_path

from . import settings as filer_settings
from . import views


urlpatterns = [
    re_path(
        filer_settings.FILER_CANONICAL_URL + r'(?P<uploaded_at>[0-9]+)/(?P<file_id>[0-9]+)/$',  # flake8: noqa
        views.canonical,
        name='canonical'
    ),
    re_path(
        filer_settings.FILER_CANONICAL_URL
        + f"(?P<slug>[{filer_settings.FILER_CANONICAL_URL_SLUG_ALLOWED_CHARS_RE}]+)/?$",  # flake8: noqa
        views.canonical_slug,
        name="canonical",
    ),
]

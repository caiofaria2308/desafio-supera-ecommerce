from uuid import uuid4 as GUID

from django.db import models
from django.utils import timezone
from django_softdelete.models import SoftDeleteModel


class BaseModel(SoftDeleteModel):
    id = models.UUIDField(
        verbose_name="ID",
        primary_key=True,
        default=GUID,
        editable=False
    )
    created_at = models.DateTimeField(
        verbose_name="Data de criação",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Data de atualização",
        auto_now=True
    )

    class Meta:
        abstract = True


def get_order_number():
    now = timezone.now()
    return f"{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}{now.microsecond}"


def get_view(url_name):
    views = get_views()
    for view in views:
        if view.name == url_name:
            return view


def get_views():
    from django.urls import URLPattern, URLResolver
    from django.urls.resolvers import RegexPattern, RoutePattern

    from main.urls import urlpatterns

    views = []
    for pattern in urlpatterns:
        if isinstance(pattern, RoutePattern) or isinstance(pattern, URLResolver):
            views.extend(get_views(pattern.url_patterns, str(pattern.pattern)))
        elif isinstance(pattern, URLPattern) or isinstance(pattern, RegexPattern):
            view = pattern.callback
            views.extend(view)
    return views

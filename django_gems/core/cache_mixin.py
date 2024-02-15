from django.views.decorators.cache import cache_page


class CachedViewMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return cache_page(1 * 3600)(view)
from django.core.cache import cache


# class CachedViewMixin:
#     @staticmethod
#     def cache_context(content):
#         if not cache.get('context'):
#             cache.set('context', content, 30)
#
#         content = cache.get('content')
#
#         return content


from django.views.decorators.cache import cache_page
class CachedViewMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return cache_page(30)(view)
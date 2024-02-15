from django.core.cache import cache
from django.views import View
from django.views.decorators.cache import cache_page

from django_gems.common.utils import get_objects_by_choices
from django_gems.jewelry.models import Category, \
    Metal, \
    StoneType, \
    StoneColor
from django_gems.wishlist.models import JewelryLike


# class CachedViewMixin:
#     @classmethod
#     def as_view(cls, **initkwargs):
#         view = super().as_view(**initkwargs)
#         return cache_page(30)(view)

class CachedViewMixin:
    @staticmethod
    def cache_context(context):
        if not cache.get('context'):
            cache.set('context', context, 30)

        context = cache.get('context')

        return context


class NavigationBarMixin(CachedViewMixin, View):

    def get_nav_bar_context(self):
        context = {}

        categories_by_choices = get_objects_by_choices(Category)

        metals_by_choices = get_objects_by_choices(Metal)

        stone_types_by_choices = get_objects_by_choices(StoneType)

        stone_colors_by_choices = get_objects_by_choices(StoneColor)

        context['categories_by_choices'] = categories_by_choices
        context['metals_by_choices'] = metals_by_choices
        context['stone_types_by_choices'] = stone_types_by_choices
        context['stone_colors_by_choices'] = stone_colors_by_choices

        # context['categories_by_choices'] = 1
        # context['metals_by_choices'] = 1
        # context['stone_types_by_choices'] = 1
        # context['stone_colors_by_choices'] = 1

        if self.request.user.pk:
            likes_count = JewelryLike.objects.filter(user_id=self.request.user.pk).count()
        else:
            likes_count = len(self.request.session.get('liked_jewelries', []))

        cart = self.request.session.get('cart', {})

        cart_count = len(cart)

        context['likes_count'] = likes_count
        context['cart_count'] = cart_count

        context = self.cache_context(context)

        # if not cache.get('context'):
        #     cache.set('context', context, 30)
        #
        # context = cache.get('context')

        return context

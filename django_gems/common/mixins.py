from django.views import View
from django_gems.common.utils import get_objects_by_choices
from django_gems.jewelry.models import (
    Category,
    Metal,
    StoneType,
    StoneColor
)
from django_gems.wishlist.models import JewelryLike
from django.core.cache import cache


class NavigationBarMixin(View):

    def get_nav_bar_context(self):
        context = {}

        categories_by_choices = get_objects_by_choices(Category)

        metals_by_choices = get_objects_by_choices(Metal)

        stone_types_by_choices = get_objects_by_choices(StoneType)

        stone_colors_by_choices = get_objects_by_choices(StoneColor)

        if self.request.user.pk:
            likes_count = JewelryLike.objects. \
                filter(user_id=self.request.user.pk).count()
        else:
            likes_count = len(self.request.session.get('liked_jewelries', []))

        cart = self.request.session.get('cart', {})

        cart_count = len(cart)

        context = {
            'categories_by_choices': categories_by_choices,
            'metals_by_choices': metals_by_choices,
            'stone_types_by_choices': stone_types_by_choices,
            'stone_colors_by_choices': stone_colors_by_choices,
            'likes_count': likes_count,
            'cart_count': cart_count,
        }

        cache.set('nav_bar_context', context, 1 * 3600)

        # if not cache.get('context'):
        #     cache.set('context', context, 1 * 3600)
        #
        # context = cache.get('context')

        # non_cached_context = {
        #     'likes_count': likes_count,
        #     'cart_count': cart_count,
        # }
        #
        # context = {
        #     'categories_by_choices': categories_by_choices,
        #     'metals_by_choices': metals_by_choices,
        #     'stone_types_by_choices': stone_types_by_choices,
        #     'stone_colors_by_choices': stone_colors_by_choices,
        #     **non_cached_context,
        # }
        #
        # cache.set('nav_bar_context', context, 1 * 3600)

        return context

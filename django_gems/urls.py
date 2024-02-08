from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('django_gems.common.urls')),
    path('', include('django_gems.jewelry.urls')),
    path('', include('django_gems.user_account.urls')),
    path('', include('django_gems.shopping_cart.urls')),
    path('', include('django_gems.order.urls')),
    path('', include('django_gems.user_profile.urls')),
    path('', include('django_gems.inventory.urls')),
    path('', include('django_gems.wishlist.urls')),

)

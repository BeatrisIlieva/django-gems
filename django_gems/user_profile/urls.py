from django.urls import path, include

from django_gems.user_profile.views import (
    UserUpdateView,
    UserDeleteView
)

urlpatterns = (
    path(
        'profile/<int:pk>/', include(
            [
                path(
                    'update/',
                    UserUpdateView.as_view(),
                    name='update_user'
                ),
                path(
                    'delete/',
                    UserDeleteView.as_view(),
                    name='delete_user'
                ),

            ]
        )
    ),
)

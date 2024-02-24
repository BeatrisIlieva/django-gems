from django.urls import path

from django_gems.common.views import (
    IndexView,
    SearchBarView, PasswordChangedSuccessfully, EmailChangedSuccessfully,
    DetailsChangedSuccessfully, ProfileDeletedSuccessfully
)

urlpatterns = (
    path(
        '',
        IndexView.as_view(),
        name='index_page'
    ),
    path(
        'search/',
        SearchBarView.as_view(),
        name='search_bar'
    ),

    path(
        'password-changed/<int:pk>/',
        PasswordChangedSuccessfully.as_view(),
        name='password_changed'
    ),

    path(
        'email-changed/<int:pk>/',
        EmailChangedSuccessfully.as_view(),
        name='email_changed'
    ),

    path(
        'details-changed/<int:pk>/',
        DetailsChangedSuccessfully.as_view(),
        name='details_changed'
    ),

    path(
        'profile-deleted/',
        ProfileDeletedSuccessfully.as_view(),
        name='profile-deleted'
    ),
)

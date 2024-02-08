from django.urls import path

from django_gems.user_account.views import (
    RegisterUserView,
    LoginOrRegisterUserView,
    LogoutUserView, CustomUpdateEmailView, CustomUpdatePasswordView
)

urlpatterns = (
    path(
        'register/',
        RegisterUserView.as_view(),
        name='register_user'
    ),
    path(
        'login-or-register/',
        LoginOrRegisterUserView.as_view(),
        name='login_or_register_user'
    ),
    path(
        'logout/',
        LogoutUserView.as_view(),
        name='logout_user'
    ),
    path(
        'update-email/<int:pk>/',
        CustomUpdateEmailView.as_view(),
        name='update_email'
    ),
    path(
        'update-password/<int:pk>/',
        CustomUpdatePasswordView.as_view(),
        name='update_password'
    ),
)

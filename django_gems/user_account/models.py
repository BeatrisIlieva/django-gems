from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django_gems.user_account.manager import AccountUserManager
from django_gems.jewelry.models import Jewelry


class AccountUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    objects = AccountUserManager()

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )


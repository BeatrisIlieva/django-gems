from django.db import models
from django.utils.translation import gettext_lazy as _

from django_gems.user_account.models import AccountUser
from django_gems.common.utils import ChoicesMaxLengthMixin

from django_gems.jewelry.models import Jewelry


class Order(models.Model):
    class StatusChoices(ChoicesMaxLengthMixin, models.TextChoices):
        P = "P", _("Pending")
        CO = "CO", _("Completed")
        CA = "CA", _("Cancelled")


    status = models.CharField(
        max_length=StatusChoices.max_length(),
        choices=StatusChoices.choices,
    )

    user = models.ForeignKey(
        to=AccountUser,
        on_delete=models.CASCADE
    )


class OrderProducts(models.Model):
    class Meta:
        unique_together = ('order', 'jewelry')

    order = models.ForeignKey(
        to=Order,
        on_delete=models.CASCADE,
    )
    jewelry = models.ForeignKey(
        to=Jewelry,
        on_delete=models.CASCADE
    )
    size = models.CharField(
        max_length=10,
    )
    quantity = models.PositiveIntegerField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

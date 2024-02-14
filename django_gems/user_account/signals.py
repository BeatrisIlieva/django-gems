from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django_gems.order.models import Order

UserModel = get_user_model()


def send_successful_registration_email(user):
    html_message = render_to_string('user-account/email-greeting.html', {'user': user})

    plain_message = strip_tags(html_message)

    send_mail(
        subject='Welcome to DjangoGems.com!',
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)


@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        total_price = calculate_total_price(instance)


        user_full_name = instance.user.accountprofile.full_name

        user_email = instance.user.email

        order_id = instance.pk
        user_country = instance.user.accountprofile.country
        user_city = instance.user.accountprofile.city
        user_address = instance.user.accountprofile.delivery_address
        user_phone_number = instance.user.accountprofile.phone_number

        html_message = render_to_string('user-account/email-order-confirmation.html', {
            'order': instance,
            'total_price': total_price,
            'user_email': user_email,
            'user_full_name': user_full_name,
            'user_country': user_country,
            'user_city': user_city,
            'user_address': user_address,
            'user_phone_number': user_phone_number,
            'order_id': order_id,

        })

        plain_message = strip_tags(html_message)

        send_mail(
            subject='Order Confirmation',
            message=plain_message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=(user_email,),
        )

def calculate_total_price(order):
    total_price = 0
    for item in order.orderproducts_set.all():
        total_price += item.total_price
    return total_price
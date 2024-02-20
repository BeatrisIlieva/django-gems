from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase as TestCase
from django_gems.order.forms import CardDetailsForm


class UserOrdersViewTests(TestCase):
    def setUp(self):
        user_data = {
            'email': 'beatris@icloud.com',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'consent': True
        }

        self.client.post(
            reverse('register_user'),
            data=user_data
        )

        self.user = get_user_model(). \
            objects.get(email=user_data['email'])

        profile_data = {
            'first_name': 'Beatris',
            'last_name': 'Ilieve',
            'phone_number': '0000000000',
            'country': 'BG',
            'city': 'Sofia',
            'delivery_address': 'Some Address',
            'user': self.user

        }

        self.client.post(
            reverse(
                'complete_order', kwargs={'pk': self.user.pk}
            ),

            data={
                **profile_data
            }
        )

        self.current_date = \
            datetime.now()

        self.current_month = \
            self.current_date.month

        self.current_year = \
            self.current_date.year

        self.one_year_behind_date = \
            self.current_date - relativedelta(years=1)

        self.one_year_behind = \
            self.one_year_behind_date.year

        self.valid_card_data = {
            'card_number': int(
                '1' * CardDetailsForm.CARD_NUMBER_LENGTH
            ),

            'expiration_date':
                f'{self.current_month:02d}/{self.current_year % 100:02d}',

            'cvv_code': int(
                '1' * CardDetailsForm.CVV_CODE_LENGTH
            )
        }

        self.client.post(
            reverse(
                'complete_transaction', kwargs={'pk': self.user.pk}
            ),
            data={
                **self.valid_card_data
            }
        )

    def test_orders_view__expect_displaying_all_orders(self):
        response = self.client.get(
            reverse(
                'order_details', kwargs={'pk': self.user.pk}
            ),
        )
        self.assertEqual(
            response.status_code, 200
        )

        self.assertIn(
            'user_pk',
            response.context
        )

        self.assertIn(
            'order_pk',
            response.context
        )

        self.assertIn(
            'country',
            response.context
        )

        self.assertIn('city', response.context)
        self.assertIn('delivery_address', response.context)
        self.assertIn('phone_number', response.context)
        self.assertIn('order_pk', response.context)

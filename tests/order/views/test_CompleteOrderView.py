from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase as TestCase


class AddToShoppingCartViewTests(TestCase):

    def test_complete_order__when_details_provided__expect_redirect(self):
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

        user = get_user_model(). \
            objects.get(email=user_data['email'])

        profile_data = {
            'first_name': 'Beatris',
            'last_name': 'Ilieve',
            'phone_number': '0000000000',
            'country': 'BG',
            'city': 'Sofia',
            'delivery_address': 'Some Address',
            'user': user
        }

        response = self.client.post(
            reverse(
                'complete_order', kwargs={'pk': user.pk}
            ),
            data={
                **profile_data
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertRedirects(response, reverse(
            'complete_transaction',
            kwargs={'pk': user.pk})
                             )

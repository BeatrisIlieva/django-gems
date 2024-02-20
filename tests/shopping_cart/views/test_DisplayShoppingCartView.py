from django.urls import reverse
from django.test import TestCase as TestCase


class DisplayShoppingCartViewTests(TestCase):

    def test_display_shopping_cart__expect__all_added_obj_to_be_displayed(self):
        response = self.client.get(
            reverse('view_shopping_cart')
        )

        self.assertEqual(
            response.status_code,
            200
        )

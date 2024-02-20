from django.test import TestCase as TestCase
from django_gems.inventory.models import Inventory
from django_gems.inventory.utils import remove_quantity_from_inventory
from django_gems.shopping_cart.models import ShoppingCart
from django_gems.shopping_cart.views import AddToShoppingCartView
from django_gems.jewelry.models import Category, Jewelry, Size, JewelrySize


class AddToShoppingCartViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title=Category.TitleChoices.NECKLACE
        )

        self.jewelry = Jewelry.objects.create(
            title='Test Jewelry',
            first_image_url='https://example.com/image1.jpg',
            second_image_url='https://example.com/image2.jpg',
            category=self.category
        )

        Inventory.objects.create(
            jewelry=self.jewelry,
            quantity=10,
            price=5
        )

        self.size = Size.objects.create(
            category=self.category,
            measurement=Size.MeasurementChoices.V_1
        )

        JewelrySize.objects.create(
            jewelry=self.jewelry,
            size=self.size
        )

        self.added_quantity_to_shopping_cart = \
            AddToShoppingCartView. \
                QUANTITY_TO_DECREASE_UPON_ADDING_TO_SHOPPING_CART

        self.added_quantity_to_shopping_cart_if_exists = \
            AddToShoppingCartView. \
                QUANTITY_TO_INCREASE_IF_EXISTING_SHOPPING_CART

    def test_add_to_shopping_cart__for_a_first_time__expect_quantity_of_one(self):
        initial_inventory_quantity = \
            Inventory.objects.get(jewelry=self.jewelry).quantity

        initial_shopping_cart_obj_count = \
            ShoppingCart.objects.count()

        ShoppingCart.objects.create(
            jewelry=self.jewelry,
            quantity=self.added_quantity_to_shopping_cart,
            size=self.size,
            order_completed=False,
            session_key=self.client.session.session_key,
        )

        remove_quantity_from_inventory(self.jewelry, self.added_quantity_to_shopping_cart)

        new_inventory_quantity = Inventory.objects. \
            get(jewelry=self.jewelry).quantity

        new_shopping_cart_quantity = ShoppingCart.objects. \
            get(jewelry=self.jewelry).quantity

        self.assertEqual(
            ShoppingCart.objects.count(),
            initial_shopping_cart_obj_count + 1
        )

        new_shopping_cart_obj = ShoppingCart.objects.last()

        self.assertEqual(
            new_shopping_cart_obj.jewelry,
            self.jewelry
        )

        self.assertEqual(
            new_inventory_quantity,
            initial_inventory_quantity - self.added_quantity_to_shopping_cart
        )

        self.assertEqual(
            new_shopping_cart_quantity,
            self.added_quantity_to_shopping_cart
        )

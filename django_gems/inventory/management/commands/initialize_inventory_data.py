import os
import django
from django.core.management.base import BaseCommand
from django_gems.inventory.models import Inventory
from django_gems.core.get_all_objects import jewelries


class Command(BaseCommand):
    help = 'Initialize data for your Django app'

    def handle(self, *args, **options):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_gems.settings")
        django.setup()

        self.stdout.write(self.style.SUCCESS('Starting data initialization...'))

        self.bulk_create_inventory()

        self.stdout.write(self.style.SUCCESS('Data initialization completed successfully.'))

    def bulk_create_inventory(self):
        jewelries_by_quantities = []

        jewelries_by_prices = [
            48000.00,
            24000.00,
            97000.00,
            37000.00,
            42000.00,
            38000.00,
            14000.00,
            27000.00,
            120000.00,
            21000.00,
            24000.00,
            32000.00,
            163000.00,
            56000.00,
            44000.00,
            33000.00,
            36000.00,
            55000.00,
            78000.00,
            49000.00,
            103000.00,
            94000.00,
            24000.00,
            42000.00,
            218000.00,
            63000.00,
            39000.00,
            97000.00,
            86000.00,
            63000.00,
            74000.00,
            43000.00,
            52000.00,
            53000.00,
            48000.00,
            33000.00,
            36000.00,
            52000.00,
            23000.00,
            57000.00,
            29000.00,
            46000.00,
        ]

        for index in range(len(jewelries)):
            jewelries_by_quantities.append(
                Inventory(
                    quantity=20,
                    jewelry=jewelries[index],
                    price=jewelries_by_prices[index]
                ),
            )

        Inventory.objects.bulk_create(jewelries_by_quantities)

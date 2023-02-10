import json

from progress.bar import Bar
from django.core.files import File
from django.core.management.base import BaseCommand

from apps.store.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("products.json", "r") as products_file:
            products = json.load(products_file)
            product: dict
            with Bar("Importing products", max=len(products)) as bar:
                for product in products:
                    photo_locale = f"assets/{product.get('image')}"
                    photo = open(photo_locale, "rb")
                    p = Product(
                        name=product.get("name"),
                        price=product.get("price"),
                        score=product.get("score"),
                        image=File(photo)
                    )
                    p.save()
                    photo.close()
                    bar.next()

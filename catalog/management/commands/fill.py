from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {'name': 'Sport', 'description': 'Sport equipment'},
            {'name': 'Household goods', 'description': 'household goods'},
            {'name': 'Software', 'description': 'OS, apps, tools'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)

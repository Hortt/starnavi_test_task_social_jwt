from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Does api calls to show how api works'

    def handle(self, *args, **options):
        pass

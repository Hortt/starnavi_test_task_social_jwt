from django.core.management.base import BaseCommand
from ...services import RandomRequestsService


class Command(BaseCommand):
    help = 'Does api calls to show how api works;' \
           'we assume this api might be placed on a different resource'

    def handle(self, *args, **options):
        RandomRequestsService().execute()

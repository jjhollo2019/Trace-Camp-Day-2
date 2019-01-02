from django.core.management.base import BaseCommand
from kick.models import KickStarter
import csv


class Command(BaseCommand):
    help = 'imports data from csv'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Path to CSV to load')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']

        with open(file_path, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if(line_count != 0):
                    KickStarter.objects.create(
                        backers_count = row[0],
                        blurb = row[1],
                        category = row[2],
                        converted_pledged_amount = row[3],
                    )
                line_count += 1

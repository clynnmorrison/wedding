from django.core.management.base import BaseCommand, CommandError
import os
import csv
from wedding.models import Rsvp
from django.contrib.auth.models import User
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        User.objects.all().delete()
        Rsvp.objects.all().delete()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "wedding_list.csv")) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                email = row[0]
                user=User.objects.create_user(email, password='password')
                for name in row[1:]:
                    Rsvp(user=user, name=name).save()
        user = User.objects.get(username="finke.dave@gmail.com")
        user.is_staff=True
        user.is_superuser=True
        user.save()

#user = User.objects.create_user("admin", password='password')
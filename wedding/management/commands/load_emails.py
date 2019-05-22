from django.core.management.base import BaseCommand, CommandError
import os
import csv
from wedding.models import Rsvp, UserProfile
from django.contrib.auth.models import User
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, "last_cousins.csv")) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                adults = row["Adults"].split("|")
                if row['Kids']:
                    kids = row["Kids"].split("|")
                else:
                    kids = []

                adults_to_use_for_name = filter(lambda adult: adult != "Plus One", adults)
                last_name = ""
                if len(adults) > 2:
                    first_name = ", ".join(adults_to_use_for_name[0:-1])
                    last_name = " and " + adults_to_use_for_name[-1]
                elif not kids:
                    first_name = adults_to_use_for_name[0]
                    if len(adults_to_use_for_name)>1:
                        last_name = " and " + adults_to_use_for_name[1]
                else:
                    if len(adults) > 1:
                        first_name = adults_to_use_for_name[0]+", "
                        last_name = adults_to_use_for_name[1] + " and Family"
                    else:
                        first_name = adults_to_use_for_name[0]
                        last_name = "and Family"

                primary_email = row["primary_email"].lstrip().rstrip()
                alternate_email = row["alternate_email"]
                if alternate_email:
                    alternate_email.lstrip().rstrip()
                address = row["Address"]

                if User.objects.filter(username=primary_email).count() > 0:
                    continue
                if len(first_name) > 30:
                    print primary_email
                    print first_name
                user = User.objects.create_user(username=primary_email, password='password', email=primary_email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                profile = UserProfile(user=user, alternate_email=alternate_email, mailing_address=address)
                profile.save()
                for adult in adults:
                    if adult == "Plus One":
                        Rsvp(user=user, is_plus_one=True).save()
                    else:
                        Rsvp(user=user, name=adult).save()
                for kid in kids:
                    Rsvp(user=user, is_child=True, name=kid).save()

#user = User.objects.create_user("admin", password='password')

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open('streets.csv', 'w') as csv_writer:
            for user in User.objects.all():
                info = []
                profile = user.userprofile_set.all()[0]

                display_name = user.first_name
                if user.last_name:
                    display_name += user.last_name

                info.append(profile)
                info.append(profile.mailing_address)

                csv_writer.writerow(info)


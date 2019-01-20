import time

from django.core.management.base import BaseCommand
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Emails the invitations'

    def handle(self, *args, **options):
        template = loader.get_template("wedding/invitation_email.html")

        for user in User.objects.filter(email='finke.dave@gmail.com'):
            print user
            profile = user.userprofile_set.all()[0]

            # if profile.sent_save_the_date or user.email.endswith('email.com'):
            #     print "Not sending to" + user.username + " already sent or bad email address"
            #     continue
            display_name = user.first_name
            if user.last_name:
                display_name += user.last_name
            html = template.render({"username": user.username, 'addressee': display_name,
                                    'host_url': settings.HOST_URL, 'start_pos': calculate_addresse_start_pos(display_name)})

            send_to = [user.email]

            if profile.alternate_email:
                send_to.append(profile.alternate_email)
            email = EmailMultiAlternatives(
                subject="Dave & Courtney's Wedding - Save the Date",
                body=html,
                from_email=settings.EMAIL_FROM,
                to=send_to,
                reply_to=settings.EMAIL_REPLY_TO)
            email.attach_alternative(html, 'text/html')
            email.send()

            profile.sent_save_the_date = True
            profile.save()

            time.sleep(120)

def calculate_addresse_start_pos(addressee):
    if len(addressee) > 40:
        percentage = 8.3
    else:
        percentage = 8.6

    return str((678 - (percentage * len(addressee))) /2)
import time

from django.core.management.base import BaseCommand
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Emails the photo links'

    def handle(self, *args, **options):
        template = loader.get_template("wedding/pictures_email.html")

        for user in User.objects.filter(username='finke.dave@gmail.com'):
            profile = user.userprofile_set.all()[0]
            if profile.sent_photos_link or user.email.endswith('email.com'):
                print "Not sending to" + user.username + " already sent or bad email address"
                continue

            html = template.render()

            send_to = [user.email]

            if profile.alternate_email:
                send_to.append(profile.alternate_email)
            email = EmailMultiAlternatives(
                subject="Dave & Courtney's Wedding - Photos",
                body=html,
                from_email=settings.EMAIL_FROM,
                to=send_to,
                reply_to=settings.EMAIL_REPLY_TO)
            email.attach_alternative(html, 'text/html')
            email.send()

            profile.sent_photos_link = True
            profile.save()
            print "Sent email to " + user.email
            time.sleep(120)

import time

from django.core.management.base import BaseCommand
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Emails the invitations'

    def handle(self, *args, **options):
        template = loader.get_template("wedding/invitation_email.html")

        for user in User.objects.filter(id__gte=331):
            print user
            profile = user.userprofile_set.all()[0]

            if profile.sent_invitation or user.email.endswith('email.com'):
                 print "Not sending to" + user.username + " already sent or bad email address"
                 continue
            html = template.render({'user_id': user.id, 'host_url': settings.HOST_URL, 'user_email': user.email})

            send_to = [user.email]

            if profile.alternate_email:
                send_to.append(profile.alternate_email)
            email = EmailMultiAlternatives(
                subject="Dave & Courtney's Wedding - Invitation",
                body=html,
                from_email=settings.EMAIL_FROM,
                to=send_to,
                reply_to=settings.EMAIL_REPLY_TO)
            email.attach_file(os.path.join(settings.BASE_DIR, "wedding", "static", "venue_directions.pdf"))
            email.attach_alternative(html, 'text/html')
            email.send()

            profile.sent_invitation = True
            profile.save()

            time.sleep(120)

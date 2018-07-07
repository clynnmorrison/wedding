from django.core.management.base import BaseCommand
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Emails the save the date'

    def handle(self, *args, **options):
        template = loader.get_template("wedding/save_the_date.html")

        user = User.objects.get(username="finke4@sbcglobal.net")
        html = template.render({"username": user.username, 'addressee': user.first_name, 'host_url': settings.HOST_URL})

        send_to = [user.email]
        profile = user.userprofile_set.all()[0]
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
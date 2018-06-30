from django.core.management.base import BaseCommand
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class Command(BaseCommand):
    help = 'Emails the save the date'

    def handle(self, *args, **options):
        template = loader.get_template("wedding/save_the_date.html")
        html = template.render({"username": 'finke.dave@gmail.com', 'host_url': settings.HOST_URL})

        email = EmailMultiAlternatives(
            subject="Dave & Courtney's wedding save the date",
            body=html,
            from_email=settings.EMAIL_FROM,
            to=["finke.dave@gmail.com"],
            reply_to=[settings.EMAIL_FROM])
        email.attach_alternative(html, 'text/html')
        email.send()
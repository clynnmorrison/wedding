from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image, ImageDraw, ImageFont
import os
class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.filter(email='finke.dave@gmail.com'):
            print user
            profile = user.userprofile_set.all()[0]


            display_name = user.first_name
            if user.last_name:
                display_name += user.last_name

            create_letter(user.id, display_name)


def create_letter(user_id, addressee):
    # create Image object with the input image
    font = ImageFont.truetype('FreeMonoOblique.ttf', size=35)
    image = Image.open(os.path.join(settings.BASE_DIR, 'static', 'empty_letter.jpg'))

    W, H = image.size

    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    w, h = draw.textsize(addressee, font=font)

    (x, y) = ((W - w) / 2, 450)
    color = 'rgb(0, 0, 0)'  # black color

    # draw the message on the background

    draw.text((x, y), addressee, fill=color, font=font)

    # draw.text((390, 450),'Dave Finke & Courtney Morrison', fill=color, font=font)


    image.save(os.path.join(settings.BASE_DIR, 'static', 'letter{}.jpg'.format(user_id)))
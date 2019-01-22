from PIL import Image, ImageDraw, ImageFont

# create Image object with the input image
font = ImageFont.truetype('FreeMonoOblique.ttf', size=35)
image = Image.open('letter.jpg')

W, H = image.size

# initialise the drawing context with
# the image object as background
   
draw = ImageDraw.Draw(image)

w, h = draw.textsize(message, font=font)

(x, y) = ((W-w)/2,450)
color = 'rgb(0, 0, 0)' # black color
 
# draw the message on the background
  
draw.text((x, y), message, fill=color, font=font)


#draw.text((390, 450),'Dave Finke & Courtney Morrison', fill=color, font=font)


image.save('letter2.jpg')

import arabic_reshaper
import pandas as pd
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

path='/Users/wafa/Desktop/My-Courses/PythonBootCamp/python-fullstack/fullstack01/يوميات شامية.csv'

df=pd.read_csv(path,encoding='utf-8')
for i,text in enumerate(df['text']):
    text_to_be_reshaped = text
    reshaped_text = arabic_reshaper.reshape(text_to_be_reshaped)
# At this stage the text is reshaped, all letters are in their correct form
# based on their surroundings, but if you are going to print the text in a
# left-to-right context, which usually happens in libraries/apps that do not
# support Arabic and/or right-to-left text rendering, then you need to use
# get_display from python-bidi.
# Note that this is optional and depends on your usage of the reshaped text.
    bidi_text = get_display(reshaped_text)
#
# At this stage the text in bidi_text can be easily rendered in any library
# that doesn't support Arabic and/or right-to-left, so use it as you'd use
# any other string. For example if you're using PIL.ImageDraw.text to draw
# text over an image you'd just use it like this...
#
# We load Arial since it's a well known font that supports Arabic Unicode
    font = ImageFont.truetype('Arial', 20)
    image = Image.new('RGBA', (2000, 600), (255,255,255))
    image_draw = ImageDraw.Draw(image)
    image_draw.text((10,10), bidi_text, fill=(0,0,0), font=font)
# Now the text is rendered properly on the image, you can save it to a file or just call `show` to see it working
    image.show()
    img_name=str(i+1)+'.PNG'
    image.save(img_name)

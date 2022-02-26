from PIL import Image, ImageFont, ImageDraw

my_image = Image.open("Picture1.png")
title_font = ImageFont.truetype('arial.ttf', 80)

title_text = "Khyatee Electronics Ltd."



image_editable = ImageDraw.Draw(my_image)
image_editable.text((50,1560), title_text, (0, 0, 0), font=title_font)

my_image.save("result.png")
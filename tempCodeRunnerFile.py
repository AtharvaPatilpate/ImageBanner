from PIL import Image, ImageFont, ImageDraw
from openpyxl import load_workbook

data_file = 'Details.xlsx'

# Load the entire workbook.
wb = load_workbook(data_file)

# Load one worksheet.
ws = wb['Sheet1']
all_rows = list(ws.rows)

# for cell in all_rows[0]:
#     print(cell.value)

for i in range(len(all_rows)):
    my_image = Image.open("Picture1.png")
    title_font = ImageFont.truetype('arial.ttf', 80)

    cell1 = all_rows[i+1][0]
    title_text1 = cell1.value

    cell2 = all_rows[i+1][1]
    title_text2 = cell2.value

    cell3 = all_rows[i+1][2]
    title_text3 = str(cell3.value)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50, 1600), title_text1, (0, 0, 0), font=title_font)
    my_image.save("result"+str(i)+".png")
    my_image = Image.open("result"+str(i)+".png")

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50, 1700), title_text2, (0, 0, 0), font=title_font)
    my_image.save("result"+str(i)+".png")
    my_image = Image.open("result"+str(i)+".png")

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((50, 1800), title_text3, (0, 0, 0), font=title_font)
    my_image.save("result"+str(i)+".png")

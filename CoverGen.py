from PIL import Image, ImageFont, ImageDraw
import os

counter = 0
songname = "Song names text file"
path = "Path to Covers"
titles = []
title_font = ImageFont.truetype('font.otf', 500)

with open(songname) as file_in:
    for line in file_in:
        titles.append(line)

for image_path in os.listdir(path):
    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    my_image = Image.open(input_path)
    image_editable = ImageDraw.Draw(my_image)
    title_text = titles[counter].strip()
    image_editable.text((0, 1250), title_text, (255, 255, 255), font=title_font)
    my_image.save("Final Covers Dir" + str(counter) + ".png")
    print("cover done")
    counter += 1

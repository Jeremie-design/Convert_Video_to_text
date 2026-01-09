#ASCII

from PIL import Image, ImageDraw , ImageFont
import math


#chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
chars = "$@B%8&WM#*oahkbUYXzcvunxrjft?-_+~<>i!lI;:,\"^`'. "
#chars = " .:;+*#%@"
charArray = list(chars)
charLength = len(charArray)
interval =  charLength/256



scaleFactor = 0.4
onecharWidth = 8
onecharHeight = 18
char_aspect_ratio = onecharWidth/onecharHeight


def getchar(inputint):
    return charArray[math.floor(inputint*interval)]

while True:
    try:
        file_name = input("What is the File? (e.g., nemo.webp)").strip().lower()
        im = Image.open(file_name).convert("RGBA")
        break
    except FileNotFoundError:
        print("file not found")
        continue
#tesst


text_file = open("output.txt", "w")

fnt = ImageFont.truetype("arial.ttf", 20)

width, height = im.size

print(width,height, height/width )
new_width = int(scaleFactor * width )
new_height = int(scaleFactor * height * char_aspect_ratio)

im = im.resize((new_width,new_height))
twidth, theight = im.size
pix = im.load()

avg_color_image = im.resize((1,1))
avg_color = avg_color_image.getpixel((0,0))
#print(avg_color)

outputImage = Image.new('RGBA', (onecharWidth * twidth, onecharHeight * theight), color = (0,0,0,0))
print(twidth,theight, theight/twidth)

d = ImageDraw.Draw(outputImage)

#print(im.mode)
#print(f"This is WxL {width},{height}")

for i in range(theight):
    for j in range(twidth):
        r, g, b, A = pix[j, i]
        #print(r)
        h = int((r + g + b)/3)
        pix[j,i] = (h, h, h)
        text_file.write(getchar(h))
        d.text((j*onecharWidth, i*onecharHeight), getchar(h), font = fnt, fill = (r,g,b))

    text_file.write('\n')
text_file.close()
outputImage.save ("output.png")
print("Converted!")



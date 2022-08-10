from PIL import Image, ImageDraw
from PIL import ImagePath
import numpy as np

im = Image.open("wire.png")
picarray = np.array(im)
size = 100
curl = size
italyimage = Image.new("RGB", (size, size))
wirecopy = Image.new("RGB", (10000, 1))
print(picarray.shape)

flag = 1
pixelcount = 0
loopcount = 0

"""pix = im.getpixel((0,0))
italyimage.putpixel((0,0), pix)
pixelcount = 1"""

while curl > 0:
    # print(curl)
    # print(pixelcount)
    for x in range(0, curl):
        pix = im.getpixel((pixelcount+x,0))
        if x+loopcount == 45:
            print(pix)
        italyimage.putpixel((x+loopcount,loopcount), pix)
    pixelcount += curl
    curl -= 1
    for y in range(0, curl):
        pix = im.getpixel((pixelcount+y,0))
        italyimage.putpixel((size-1-loopcount,y+1+loopcount), pix)
    pixelcount += curl
    # no change to curl
    if pixelcount == 10000:
        break
    for x in range(0, curl):
        pix = im.getpixel((pixelcount+x,0))
        italyimage.putpixel((size-x-loopcount-2,size-1-loopcount), pix) #reverse it though
    pixelcount += curl
    curl -= 1
    for y in range(0, curl):
        pix = im.getpixel((pixelcount+y,0))
        italyimage.putpixel((loopcount,size-y-2-loopcount), pix)
    pixelcount += curl
    # no change to curl
    loopcount += 1

italyimage.show()
italyimage.save("italy.jpg")




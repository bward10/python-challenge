from PIL import Image
import requests
import urllib.request

im = Image.open("balloons.jpg")
rgb_im = im.convert('RGB')

xsize = im.size[0]
halfx = im.size[0] // 2
ysize = im.size[1]

newpic = Image.new("RGB", (xsize + halfx, ysize))

for y in range(ysize):
    #print()
    for x in range(halfx):
        pix1 = rgb_im.getpixel((x,y))
        pix2 = rgb_im.getpixel((x+(halfx),y))
        pixlist = (pix1[0]-pix2[0], pix1[1]-pix2[1], pix1[2]-pix2[2])
        newpic.putpixel((x,y), pix1)
        newpic.putpixel((x+halfx,y), pixlist)
        newpic.putpixel((x+xsize,y), pix2)

        # if x % 100 == 0 and y % 100 == 0:
        #     print(pix1, pixlist, pix2)
        #     print(pix1[0]+pix1[1]+pix1[2], pix2[0]+pix2[1]+pix2[2])
  

newpic.show()
newpic.save("newballoons.jpg")



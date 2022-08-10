from PIL import Image, ImageDraw
from PIL import ImagePath
import numpy as np

im = Image.open("mozart.gif")
rgb_im = im.convert('RGB')
picarray = np.array(im)
newx = 639

newmoz = Image.new("RGB", (640, 480))

print(picarray.shape)
print(im.size)

print(rgb_im.getpixel((431, 0)))

for y in range(im.size[1]):
    #print()
    for x in range(im.size[0]):
        pix = rgb_im.getpixel((x,y))
        if pix == (255, 0, 255):
            newx = x
            for x2 in range(im.size[0]):
                pix = rgb_im.getpixel((x2,y))
                newmoz.putpixel((x2-newx,y), pix)
            break

"""for y in range(im.size[1]):
    #print()
    for x in range(im.size[0]):
        pix = rgb_im.getpixel((x,y))
        if pix == (255, 0, 255):
            newx = 640 - x
            for x2 in range(im.size[0]):
                pix = rgb_im.getpixel((x2,y))
                newmoz.putpixel((newx+x2,y), pix)
            break"""

"""for y in range(im.size[1]):
    #print()
    for x in range(im.size[0]):
        pix = rgb_im.getpixel((x,y))
        if pix == (255, 0, 255):
            for x2 in range(im.size[0]):
                pix = rgb_im.getpixel((x2,y))
                newmoz.putpixel((x2-x,y), pix)
            break
       """

"""for y in range(im.size[1]):
    #print()
    for x in range(im.size[0]):
        pix = rgb_im.getpixel((x,y))
        if pix == (255, 0, 255):
            if x > 319:
                for x2 in range(im.size[0]):
                    pix = rgb_im.getpixel((x2,y))
                    newmoz.putpixel((x2-x,y), pix)
            else:
                for x3 in range(im.size[0]):
                    pix = rgb_im.getpixel((x3,y))
                    newmoz.putpixel((x-x3,y), pix)
            break"""
       

newmoz.show()
newmoz.save("newmoz.jpg")



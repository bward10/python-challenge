from PIL import Image, ImageDraw
from PIL import ImagePath
import numpy as np

im = Image.open("cave.jpg")
# im.show()

# r, g, b = im.getpixel((1, 1))

# print(r, g, b)

#print(im.format, im.size, im.mode)

#picarray = np.array()
#picarray = []
#print(im.getpixel((0, 0)))

picarray = np.array(im)

#print(len(picarray))

imx = im.size[0]
imy = im.size[1]

print(imx // 2, imy // 2)

print(picarray.shape)
# print(picarray[0, 0])
# print(picarray[1, 0])
# print(picarray.size)
# print("Program Starts Here:")

#xoyoarray = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]))
xoyoarray = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)
xeyearray = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)

outimage0 = Image.new("RGB", (640, 480))
outimage1 = Image.new("RGB", (640, 480))
# outimage.show()


#print(xoyoarray[2,3])

# print(picarray)
# print(picarray[479,0,1])

flag = 0
for y in range(picarray.shape[0]):
    # print(y)
     for x in range(picarray.shape[1]):
        #print(x,y)
        #print(im.getpixel((x,y)))
        if y % 2 == 0:
            if x % 2 == 0:
                pix = im.getpixel((x,y))
                outimage0.putpixel((x,y), pix)
            else:
                pix = im.getpixel((x,y))
                outimage1.putpixel((x,y), pix)
        else:
            if x % 2 == 0:
                pix = im.getpixel((x,y))
                outimage1.putpixel((x,y), pix)
            else:
                pix = im.getpixel((x,y))
                outimage0.putpixel((x,y), pix)

outimage0.show()
outimage1.show()

outimage0.save("5808.jpg")

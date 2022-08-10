from PIL import Image, ImageDraw
from PIL import ImagePath
import numpy as np

im = Image.open("evil1.jpg")
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
color1array = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)
color2array = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)
color3array = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)

outimage0 = Image.new("RGB", (640, 480))
outimage1 = Image.new("RGB", (640, 480))
outimage2 = Image.new("RGB", (640, 480))
outimage3 = Image.new("RGB", (640, 480))
outimage4 = Image.new("RGB", (640, 480))
outimage5 = Image.new("RGB", (640, 480))

"""
#xoyoarray = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]))
xoyoarray = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)
xeyearray = np.zeros(shape=(picarray.shape[0], picarray.shape[1], picarray.shape[2]), dtype=int)

outimage0 = Image.new("RGB", (640, 480))
outimage1 = Image.new("RGB", (640, 480))
# outimage.show()
"""

#print(xoyoarray[2,3])

# print(picarray)
# print(picarray[479,0,1])


# # two splits in x
# flag = 0
# for x in range(picarray.shape[1]):
#     if flag == 0:
#         for y in range(picarray.shape[0]):
#             pix = im.getpixel((x,y))
#             outimage0.putpixel((x,y), pix)
#         flag = 1
#     elif flag == 1:
#         for y in range(picarray.shape[0]):
#             pix = im.getpixel((x,y))
#             outimage1.putpixel((x,y), pix)
#         flag = 0



# six splits in y
flag = 0
for y in range(picarray.shape[0]):
    if flag == 0:
        for x in range(picarray.shape[1]):
            pix = im.getpixel((x,y))
            outimage0.putpixel((x,y), pix)
        flag = 1
    elif flag == 1:
        for x in range(picarray.shape[1]):
            pix = im.getpixel((x,y))
            outimage1.putpixel((x,y), pix)
        flag = 2
    elif flag == 2:
        for x in range(picarray.shape[1]):
            pix = im.getpixel((x,y))
            outimage2.putpixel((x,y), pix)
        flag = 3
    elif flag == 3:
        for x in range(picarray.shape[1]):
            pix = im.getpixel((x,y))
            outimage3.putpixel((x,y), pix)
        flag = 4
    elif flag == 4:
        for x in range(picarray.shape[1]):
            pix = im.getpixel((x,y))
            outimage3.putpixel((x,y), pix)
        flag = 5
    else:
        for x in range(picarray.shape[1]):
            pix = im.getpixel((x,y))
            outimage4.putpixel((x,y), pix)
        flag = 0




# flag = 0
# for y in range(picarray.shape[0]):
#     # print(y)
#      for x in range(picarray.shape[1]):
#         if flag == 0:
#             pix = im.getpixel((x,y))
#             outimage0.putpixel((x,y), pix)
#             flag = 1
#         elif flag == 1:
#             pix = im.getpixel((x,y))
#             outimage1.putpixel((x,y), pix)
#             flag = 2
#         else:
#             pix = im.getpixel((x,y))
#             outimage2.putpixel((x,y), pix)
#             flag = 0
            

        #print(x,y)
        #print(im.getpixel((x,y)))
        #if y % 2 == 0:
        # if y % 3 == 0:
        #     if y == 303:
        #         pix = im.getpixel((x,y))
        #         outimage0.putpixel((x,y), pix)
        #     else:
        #         if x % 2 == 0:
        #             pix = im.getpixel((x,y))
        #             outimage0.putpixel((x,y), pix)
        #         else:
        #             pix = im.getpixel((x,y))
        #             outimage1.putpixel((x,y), pix)

        # else:
        #     if x % 2 == 0:
        #         pix = im.getpixel((x,y))
        #         outimage1.putpixel((x,y), pix)
        #     else:
        #         pix = im.getpixel((x,y))
        #         outimage0.putpixel((x,y), pix)

outimage0.show()
outimage1.show()
outimage2.show()
outimage3.show()
outimage4.show()
outimage5.show()

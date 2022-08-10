from PIL import Image, ImageDraw
from PIL import ImagePath
import numpy as np

data = open("evil2.gfx", "rb").read()
#print(data)
print(len(data))

num = 5

outimage0 = Image.new("RGB", (640, 480))
outimage1 = Image.new("RGB", (640, 480))
outimage2 = Image.new("RGB", (640, 480))
outimage3 = Image.new("RGB", (640, 480))
outimage4 = Image.new("RGB", (640, 480))


for i in range(5):
    open('outimage%d.jpg' %i,'wb').write(data[i::5])

for i in range(5):
    im = Image.open('outimage%d.jpg' %i)
    im.show()


for i in range(5):
    ('%d.jpg' % i).show()


# bytes = []
# for j in range(len(data)//num):
#     for i in range(num):
#         print(data[j+i])
#         list0[j].write(data[j+1])
#         list1 = []
#         list2 = []
#         list3 = []
#         list4 = []
#         # bytes = data[i]
#         # print(bytes)

# print(data.read(0))

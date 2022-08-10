from PIL import Image
#from numpy import array
im = Image.open("oxygen.png")
# im.show()


#print(im.format, im.size, im.mode)
#print(im.size[1] / 2)

#print(array(im))



for x in range(1, 628, 7):
    pix = im.getpixel((x, 50))
    #print(x, end="")
    #print(pix)
    #print(pix[0], end="")
    char = chr(pix[0])
    print(char, end="")
    
# #Step 2:
# next_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]
# print()
# for i in next_level:
#     print(chr(i), end="")

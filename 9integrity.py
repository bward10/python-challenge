from PIL import Image, ImageDraw
from PIL import ImagePath
import bz2

#from numpy import array
im = Image.open("integrity.JPG")
# im.show()


print(im.format, im.size, im.mode)
#print(im.size[1] / 2)

#print(array(im))

coords=[179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282]
#print(len(coords))

coords_list = []

for x in range(0, 131, 2):
    xy = (coords[x], coords[x+1])
    pix = im.getpixel(xy)
    coords_list.append(xy)
    #print(x, end="")
    #print(pix)
    #print(pix, end=", ")
    #char = chr(pix[0])
    #print(char, end="")
    
#print(coords_list)

# img = Image.new("RGB", im.size, "#f9f9f9") 
# imga = ImageDraw.Draw(img)  
# imga.polygon(coords_list, fill ="#eeeeff", outline ="blue") 
# img.show()
# img.save("outline.jpg")

#img = Image.new("RGB", im.size, "#f9f9f9") 
img = ImageDraw.Draw(im)  
img.polygon(coords_list, fill ="#eeeeff", outline ="blue") 
im.show()
im.save("integrityoutline.jpg")

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(un))
print(bz2.decompress(pw))
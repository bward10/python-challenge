import zipfile

dir_name = "channelzips"

"""
with zipfile.ZipFile("channel.zip", "r") as zip_ref:
    zip_ref.extractall(dir_name)
"""
#only need to unzip once
"""
filename = "readme"
file = open(dir_name + "/" + filename + ".txt",'r')
print(file.read())
"""
#only need to read this once

archive = zipfile.ZipFile("channel.zip", 'r')

nothing = "90052"
commentcollector = "channelcomments.txt"
open(commentcollector, "w").close()

for i in range(908):
    parse_filename = dir_name + "/" + nothing + ".txt"
    file = open(parse_filename, "r")
    text = str(file.read())
    nothing = text[text.rfind(" ")+1:len(text)]
    #print(archive.getinfo(nothing + ".txt").comment, end="") #Step 2
    file1 = open(commentcollector, 'a')
    a = str(archive.getinfo(nothing + ".txt").comment)[2]
    if a == "\\":
        file1.write("\n")
    else:
        file1.write(a)
    
    #print(text)
    # if text.find("") > 0:
    #     print("comment")
    #     print(nothing)
    #print(nothing)
file1.close()
parse_filename = dir_name + "/" + nothing + ".txt"
file = open(parse_filename,"r")
print("The text from " + nothing + ".txt: " + file.read())




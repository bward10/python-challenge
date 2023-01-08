import gzip
import difflib

# writes the data into a text file
f = gzip.open('deltas.gz', 'rb')
# print(f.read())
txtfile = "balloonstext.txt"
t = open(txtfile, "wb")
t.write(f.read())
t.close()
f.close()

t = open(txtfile, "rb")
databyline = t.readlines()
t.close()

txtsplit1 = "balloonstext1.txt"
t1 = open(txtsplit1, "wb")
txtsplit2 = "balloonstext2.txt"
t2 = open(txtsplit2, "wb")

for line in databyline:
    t1.write(line[:53].strip()+b'\n') #strips may be unnecessary, especially for t2
    t2.write(line[56:].strip()+b'\n')

t1.close()
t2.close()

t1txt = open(txtsplit1, "r")
t1txtlines = t1txt.readlines()
t2txt = open(txtsplit2, "r")
t2txtlines = t2txt.readlines()

txtdiff = "balloonstextdiff.txt"
tdiff = open(txtdiff, "w")

columndifference = difflib.Differ().compare(t1txtlines, t2txtlines)
difflist = list(columndifference)

diffstr = ""
for line in difflist:
    diffstr += line

tdiff.write(diffstr)
tdiff.close()
t1txt.close()
t2txt.close()

tdiffr = open(txtdiff, "r")

plusstr = b''
minstr = b''
neitherstr = b''

pic1 = open("balloon1.png", "wb")
pic2 = open("balloon2.png", "wb")
pic3 = open("balloon3.png", "wb")

diffrlines = tdiffr.read()
diffrsplit = diffrlines.splitlines()
for line in diffrsplit:
    linedata = bytes.fromhex((line[2:]))
    if line[0] == "+":
        pic1.write(linedata)
        plusstr += line[2:].strip().encode()+ b'\n'
    elif line[0] == "-":
        pic2.write(linedata)
        minstr += line[2:].strip().encode()+ b'\n'
    else:
        neitherstr += line[2:].strip().encode()+ b'\n'
        pic3.write(linedata)

#everything here is unnecessary. so are the other lines
tb1 = open("balloons1.txt", "wb")
tb2 = open("balloons2.txt", "wb")
tb3 = open("balloons3.txt", "wb")

tb1.write(plusstr)
tb1.close()
tb2.write(minstr)
tb2.close()
tb3.write(neitherstr)
tb3.close()

pic1.close()
pic2.close()
pic3.close()





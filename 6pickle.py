import pickle

ifilename = "banner.p" #must be in the base directory that the terminal is using
infile = open(ifilename,'rb')

"""
ofilename = "pythonbytes.txt"
outfile = open(ofilename, "wb")
"""

#print(pickle.load(infile)) #unpickling the file

result = pickle.load(infile)
for i in result:
    for j in i:
        for k in range(j[1]): #this gives me the number part of the dict
            print(j[0], end="") #prints the character in the first part of the dict, end="" prevents it from printing everyting on a new line
    print() #puts a new line



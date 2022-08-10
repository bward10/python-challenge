num = "1"
print("startnum = ", num)
nextnum = ""

# count = 1
numrange = 9
a = [] #might want to put num in here and move the append call to the end of the loop.

for j in range(numrange):
    count = 1
    a.append(num)
    for i in range(len(num)):
        #i lags behind (starts at 0) so I'm adding 1 to it later
        if i+1 < len(num) and num[i] == num[i+1]: #Am I getting to the end of the string and is the next character the same?
            count +=1         
        else:
            nextnum += str(count)
            nextnum += num[i]
            count = 1 #resetting just in case

        # print("i = ", i, ", i+1= ", i+1)
        #print("looking at number ", num[i])
        #print("count = ", count)
        # print("nextnum = ", nextnum)
    #print("nextnum = ", nextnum)
    num = nextnum
    nextnum = ""

print(a)
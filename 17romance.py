
from ast import parse
# from curses.ascii import isdigit
import urllib.request
import urllib.parse
import bz2

"""# Step 1
# initialize a session
session = requests.Session()

# send a get request to the server
# I'm looking at the linkedlist (#5) to see if there's a cookie
response = session.get('http://www.pythonchallenge.com/pc/def/linkedlist.php')
  
# print the response dictionary
print("cookie from the main php = ", end="")
print(session.cookies.get_dict())
# response: you%20should%20have%20followed%20busynothing..."""

# Step 2:
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
busynothing = "12345"


"""#found where the data is with this:
parse_url = url + busynothing
x = urllib.request.urlopen(parse_url)
raw = x.read().decode("utf-8")
print("raw here:", end=" ")
print(raw)
header = x.getheader("Set-Cookie")
loc = header.find("info=")
print(header)
print(header[loc+5])"""

# x = urllib.request.urlopen(url)
# text = str(x.read()) #this seems to turn x into a string. Avoid.
# print(text[text.rfind(" ")+1:len(text)-1])


loopvar = 1000
jar = ""

for i in range(0, loopvar):
    parse_url = url + busynothing
    x = urllib.request.urlopen(parse_url)
    raw = x.read().decode()
    # raw = x.read().decode("utf-8")
    #print("raw here:", end=" ")
    #print(raw)
    header = x.getheader("Set-Cookie")
    print(header)

    loc = header.find("info=")
    loc2 = header.find(";")
    #print(header[loc+5:loc2])
    if header[loc+5:loc2] == "deleted":
        break
    jar += header[loc+5:loc2]
    # # text = str(x.read())
    # #print(x.read().decode("utf-8"))
    busynothing = raw[raw.rfind(" ")+1:len(raw)]
    # #print(busynothing)


    if raw == None:
        break

print(jar)
answer = urllib.parse.unquote_to_bytes(jar)
print(bz2.decompress(answer))



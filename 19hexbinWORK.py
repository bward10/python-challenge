import urllib.request
import requests
from bs4 import BeautifulSoup
import wave
import base64


url = "http://www.pythonchallenge.com/pc/hex/bin.html"
username = 'butter'
password = 'fly'

html_doc = requests.get(url, auth=(username, password)).content
soup = BeautifulSoup(html_doc, 'html.parser')
# print(html_doc)
# print(soup.prettify())
# print(email.message_from_string(str(html_doc)))


txtfile = "hexbin.txt"
t = open(txtfile, "wb") #just w if it's actual text for once
t.write(html_doc)
print(len(html_doc))
t.close()

message = "hexbinmessage.txt"
t1 = open(message, "wb")
t1.write(html_doc[635:151421])
t1.close()


t1 = open(message, "rb")
databyline = t1.readlines()
t1.close()
msgstrip = "hexbinstrip.txt"
t2 = open(msgstrip, "wb")
for line in databyline:
    t2.write(line.strip()) 
t2.close()

t2 = open(msgstrip, "rb")
wavfile = 'hexbin.wav'
w = wave.open(wavfile, 'w')
w.write(base64.b64decode(t2.read()))
w.close()


# msgnoline = "hexbinmsgnoline.txt"
# t2 = open(msgnoline, "wb")
# t2.write(html_doc[635:151421])
# t2.close


# b64msg = "".join(html_doc.text.split("--===============1295515792==").split('\n')[4:-2])
# print(b64msg)

# message = "hexbinmessage.txt"
# t1 = open(message, "wb")
# t1.write(html_doc[555:151425]) #try changing to 151421
# t1.close



# t1 = open(message, "rb")
# databyline = t1.readlines()
# t1.close()
# print(databyline)




# for line in databyline:
#     if isinstance(line, bytes):
#         t1.write(line)







# text = str(f.read())

# print(text)

"""
x = urllib.request.urlopen(url)
text = str(x.read())
print(text)
"""


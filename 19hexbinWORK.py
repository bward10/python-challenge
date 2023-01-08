import urllib.request
import requests
from bs4 import BeautifulSoup
import wave
import base64
import soundfile
import struct
import numpy as np


url = "http://www.pythonchallenge.com/pc/hex/bin.html"
username = 'butter'
password = 'fly'

# html_doc = requests.get(url, auth=(username, password)).content
html_doc = requests.get(url, auth=(username, password))
# soup = BeautifulSoup(html_doc, 'html.parser')
# print(html_doc)
# print(soup.prettify())
# print(email.message_from_string(str(html_doc)))

b64msg = "".join(html_doc.text.split("--===============1295515792==")[-2].split('\n')[4:-2])
res = bytes(b64msg, 'utf-8') #for some reason I have to make it bytes
dec = base64.b64decode(res)

w = open('hexbin.wav', 'wb')
#w.write(b64msg)
w.write(dec)
w.close()

#print(dec)
#soundfile.write('hexbin2.wav', dec, '11025')

# data, samplerate = soundfile.read('hexbin.wav')
# print(samplerate)


x = soundfile.SoundFile('hexbin.wav')
# print(x.mode)
# print(x.samplerate)
print(x.channels)
# print(x.subtype)
# print(x.endian)
# print(x.format)
#print(x.read(3))
#print(type(x.read()))
#print(x.buffer_read(3))
#soundfile.SoundFile('hexbin.wav').read()
# data = x.read()
# print(data)

#print(soundfile.read('hexbin.wav', -1, 0, None, 'float64', False, None, None, None, None, None, None, None, 'big'))
#print(soundfile.read('hexbin.wav', -1, -1, -1, 'float64', False, None, None, None, None, None, None, None, 'big'))
#print(soundfile.read('hexbin.wav', -1, 0))
data, samplerate = soundfile.read('hexbin.wav')
print(data, samplerate)
#print(data.byteswap(True))
#print(data.view(np.uint8))
newdata = data.newbyteorder().byteswap()
#print(newdata.view(np.uint8))

print(x.subtype)

soundfile.write('indian.wav', newdata, samplerate, x.subtype, 'big', x.format)
y = soundfile.SoundFile('indian.wav')
# print(y.mode)
# print(y.samplerate)
# print(y.subtype)
# print(y.endian)
# print(y.format)
# print(y.read(3))
x = soundfile.SoundFile('hexbin.wav')
# print(x.read(3))
# print(y.read(3))






# txtfile = "hexbin.txt"
# t = open(txtfile, "wb") #just w if it's actual text for once
# t.write(html_doc)
# print(len(html_doc))
# t.close()

# message = "hexbinmessage.txt"
# t1 = open(message, "wb")
# t1.write(html_doc[635:151421])
# t1.close()


# t1 = open(message, "rb")
# databyline = t1.readlines()
# t1.close()
# msgstrip = "hexbinstrip.txt"
# t2 = open(msgstrip, "wb")
# for line in databyline:
#     t2.write(line.strip()) 
# t2.close()

# t2 = open(msgstrip, "rb")
# wavfile = 'hexbin.wav'
# w = wave.open(wavfile, 'w')
# w.write(base64.b64decode(t2.read()))
# w.close()


# msgnoline = "hexbinmsgnoline.txt"
# t2 = open(msgnoline, "wb")
# t2.write(html_doc[635:151421])
# t2.close




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


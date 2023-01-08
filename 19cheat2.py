import requests
import base64
import soundfile

url = 'http://www.pythonchallenge.com/pc/hex/bin.html'

response = requests.get(url, auth=('butter', 'fly'))

b64 = "".join(response.text.split("--===============1295515792==")[-2].split('\n')[4:-2])

h = open('indian.wav', 'w')
h.write(base64.b64decode(b64))
h.close()

indian = soundfile.SoundFile('indian.wav')
soundfile.write('something.wav', indian.read(), indian.subtype, 'BIG', indian.format)
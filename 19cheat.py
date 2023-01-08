
import requests
import wave
import base64


url = "http://www.pythonchallenge.com/pc/hex/bin.html"
username = 'butter'
password = 'fly'

html_doc = requests.get(url, auth=(username, password))

b64msg = "".join(html_doc.text.split("--===============1295515792==")[-2].split('\n')[4:-2])
print(b64msg)
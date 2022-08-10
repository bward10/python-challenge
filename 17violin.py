import urllib.request
import urllib.parse
import requests



# Step 1
# initialize a session
s = requests.Session()

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
msg = 'the flowers are on their way'

r = requests.get(url)

response = s.get(url)
  
# print the response dictionary
print(s.cookies.get_dict())


req = urllib.request.Request(url, headers={"Cookie":"info="+msg})


print(urllib.request.urlopen(req).read())
print(r.cookies)


# jar = cookielib.CookieJar()
# req = requests.get(url, cookies=jar)

# print(jar)

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


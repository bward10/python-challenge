from ast import parse
import urllib.request
import urllib.parse

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

nothing = "12345"


for i in range(0, 400):
    parse_url = url + nothing
    x = urllib.request.urlopen(parse_url)
    text = str(x.read())
    nothing = text[text.rfind(" ")+1:len(text)-1]
    # if i >= 370:
    #     print(i)
    #     print(nothing)
    if nothing.isnumeric() == False:
        print(i)
        print(nothing)


# x = urllib.request.urlopen(url)
# text = str(x.read())

#print(text.rfind(" "))
#print(len(text))
#print(text[text.rfind(" ")+1:len(text)-1])


"""
parse_url = urllib.parse.urlparse(url)
print(parse_url)
print(parse_url.query)
"""


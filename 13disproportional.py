#http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')

# Print list of available methods
print(s.system.listMethods())
#s.phone("3845")
print(s.phone("Bert")) # for the answer to pc 17, put in Leopold
#print(s.system.methodHelp(s.phone()))
print(s.system.methodHelp("phone"))
print(s.system.methodSignature("phone"))
#print(s.system.getCapabilities("phone"))

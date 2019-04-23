# python challenge 13
import xmlrpc.client
with xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php") as proxy:
    print(proxy.system.listMethods())
    print(proxy.system.methodHelp('phone'))
    print(proxy.phone('Bert'))

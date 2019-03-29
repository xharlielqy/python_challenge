import pickle
from urllib.request import urlopen

object = pickle.load(urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))


print(object)
for line in object:
    print("".join([k * v for k, v in line]))

import requests
import re

url_address = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = '8022'
while 1:
    r = requests.get(url=url_address + num)
    html = r.text
    print(html)
    pattern = re.compile(r'\b\d+\b')
    match = pattern.findall(html)
    if match:
        print(match[-1])
        num = match[-1]
    else:
        break

import requests
import re

url_address = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = '63579'
while 1:
    r = requests.get(url=url_address + num)
    html = r.text
    pattern = re.compile(r'\b\d+\b')
    match = pattern.findall(html)
    print(html)
    print(match[0])
    num = match[0]

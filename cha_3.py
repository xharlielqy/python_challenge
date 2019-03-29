# python challenge 3, this challenge need to you study regular expression
import re

f = open('cha_3', 'r')  # open the file
content = f.read()
pattern = re.compile(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
match = pattern.findall(content)
print(match)
text = ''
for word in match:
    text = text + word[4]
print(text)

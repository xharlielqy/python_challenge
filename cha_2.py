# python challenge 2
import string

f = open('cha_2', 'r')
text = ''

for line in f:
    for word in line:
        if word in string.ascii_lowercase:
            text = text + word
print(text)

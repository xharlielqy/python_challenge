# python challenge 6
import zipfile
import re

f = zipfile.ZipFile("channel.zip")
num = '90052'
comments = []
while 1:
	content = f.read(num + ".txt").decode("utf-8")
	comments.append(f.getinfo(num + '.txt').comment.decode('utf-8'))
	print(content)
	match = re.search("\b\d+\b", content)
	if match == None:
		break
	num = match.groups(1)[0]

print(''.join(comments))

# python challenge 7
from PIL import Image
im = Image.open('oxygen.png')
text = []
message = ''
print(im.format, im.size, im.mode)
# from result above the size of image is (629,95)
width = im.size[0]
for i in range(88):
    pixel = im.getpixel((7 * i, 48))  # the width of each grey block is 7
    text.append(pixel[0])
print(text)

for num in text:
    letter = chr(num)
    message = message + letter
print(message)
# the message is 105, 110, 116, 101, 103, 114, 105, 116, 121
new_message = [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_level = ''.join(chr(num) for num in new_message)
print(next_level)

# python challenge 11
from PIL import Image

im = Image.open("cave.jpg")

(w, z) = im.size
odd = Image.new('RGB', (w // 2, z // 2))
even = Image.new('RGB', (w // 2, z // 2))

for i in range(w):
    for j in range(z):
        p = im.getpixel((i, j))
        if (i + j) % 2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

even.show()
odd.show()

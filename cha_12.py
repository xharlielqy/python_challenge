# python challenge 12

content = open('evil2.gfx', "rb").read()
for i in range(5):
    open('%d.jpg' % i, 'wb').write(content[i::5])

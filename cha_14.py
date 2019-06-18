# Python challenge 14
from functools import reduce
from PIL import Image
lis = [[i, i - 1, i - 1, i - 2] for i in range(100, 1, -2)]
lis = reduce(lambda x, y: x + y, lis)

org = Image.open('14.png')
org_data = list(org.getdata())
res = Image.new(org.mode, (100, 100))
res_data = res.load()
dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]

v = 0
org_index = 0
res_pos = (-1, 0)
for times in lis:
    for i in range(times):
        res_pos = tuple(map(lambda x, y: x + y, res_pos, dire[v]))
        res_data[res_pos] = org_data[org_index]
        org_index += 1
    v = (v + 1) % 4
res.save('rs.png')

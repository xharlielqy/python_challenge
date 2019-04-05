# python challenge 10, a = [1,11,21,1211,111221,...] len(a[30])
list = [1]
new_list = []
for times in range(30):
    count = 1
    previous_num = list[0]
    for number in list[1:]:
        if number == previous_num:
            count = count + 1
        else:
            new_list.append(count)
            count = 1
            new_list.append(previous_num)
            previous_num = number
    new_list.append(count)
    new_list.append(previous_num)
    list = new_list
    new_list = []
print(len(list))

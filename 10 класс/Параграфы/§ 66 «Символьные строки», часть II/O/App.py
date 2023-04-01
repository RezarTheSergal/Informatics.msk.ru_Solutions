def get_used_digits(string, array):
    for i in range(len(string)):
        if string[i].isdigit():
            array.append(int(string[i]))
    return sorted(array)

             
string = input()
dictionary = list(range(10))
array = get_used_digits(string, list())

temp = [4294967295]*10
for i in dictionary:
    if i in array:
        temp[i] = array.count(i)


integer = ""
for i in range(10):
    if min(temp) < 4294967295:
        index = temp.index(min(temp))
        temp[index] = 4294967295
        integer += str(index)


print(integer)

a = input()
counter = len(a)
array = [i for i in a]

for i in range(len(array)):
    if array[i] == 'a':
        array[i] = 'b'
    elif array[i] == 'b':
        array[i] = 'a'
    elif array[i] == 'A':
        array[i] = 'B'
    elif array[i] == 'B':
        array[i] = 'A'
    else:
        counter -= 1

print(*array, sep="")
print(counter)

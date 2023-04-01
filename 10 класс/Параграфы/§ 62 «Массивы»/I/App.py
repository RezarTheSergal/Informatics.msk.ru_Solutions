num = int(input())
if num < 2:
    print(1)
else:
    array = [1, 1]

    for i in range(1, num - 1):
        array.append(array[i] + array[i - 1])
    print(*array)

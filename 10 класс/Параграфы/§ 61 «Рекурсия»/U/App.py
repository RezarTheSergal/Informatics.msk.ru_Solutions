def MaxCount(array = [], i = 0, number = -2147483647):
    if number != 0:
        number = int(input())
        if number != 0:
            array.append(number)
        return MaxCount(array, i + 1, number)
    else:
        if i == 1 and number == 0:
            return 0
        return round(sum(array) / len(array), 3)

print(MaxCount())

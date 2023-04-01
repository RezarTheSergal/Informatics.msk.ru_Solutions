import random as rnd

first, last, num = list(map(int, input().split()))
array = [rnd.randint(first, last) for i in range(num)]

print(*array)
cntrEven = 0
cntrOdd = 0
for i in array:
    if i % 2 == 0:
        cntrEven += 1
    else:
        cntrOdd += 1

print(cntrEven, cntrOdd)

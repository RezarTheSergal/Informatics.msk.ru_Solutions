import random as rnd

first, last, num = list(map(int, input().split()))
array = [rnd.randint(first, last) for i in range(num)]

print(*array)
maximum = -1
for i in array:
    if i > 0 and i % 2 == 0 and maximum < i:
        maximum = i

print(maximum)

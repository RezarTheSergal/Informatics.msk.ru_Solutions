N = int(input())
array = list(map(int, input().split()))
move = int(input())
answ = list()

for i in range(move):
    array.append(array[i])
    array[i] = -2147483647

for i in array:
    if i != -2147483647:
        answ.append(i)

print(*answ)

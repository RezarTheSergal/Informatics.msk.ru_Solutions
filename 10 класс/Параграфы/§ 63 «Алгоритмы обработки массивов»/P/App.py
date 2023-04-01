N = int(input())
array = list(map(int, input().split()))
answ = list()
counter = 0
for i in array:
    if i != 0:
        answ.append(i)
    else:
        counter += 1
for i in range(counter):
    answ.append(0)

print(*answ)

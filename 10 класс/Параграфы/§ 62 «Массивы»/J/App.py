from random import randint

first, last, N = map(int, input().split())
array = list()

for i in range(N):
    array.append(randint(first, last))

counter = 0
for i in array:
    print(i, end=" ")
    if abs(i) // 10 % 10 % 2 == 0:
        counter += 1
   
print()
print(counter)

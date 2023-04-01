from random import randint

first, last, N = map(int, input().split())
array = list()

for i in range(N):
    array.append(randint(first, last))

counter = 0
for i in array:
    if i > 99 and i < 1000 and i % 5 != 0:
        counter += 1
    print(i, end=" ")
    
print()
print(counter)

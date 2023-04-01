a = []
n1 = int(input())

for i in range(1, n1+1):
    a.append(2**i)

for i in reversed(a):
    print(i, end=" ")

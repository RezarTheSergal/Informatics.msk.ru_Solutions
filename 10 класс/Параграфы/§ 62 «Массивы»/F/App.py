a = []
n1, n2 = map(int, input().split())

for i in range(n1+n2-1, n1-1, -1):
    a.append(i)

for i in a:
    print(i, end=" ")

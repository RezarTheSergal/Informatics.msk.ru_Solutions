a, b = map(int, input().split())
c, d = map(int, input().split())
temp = 0
for i in range(10000, 100000):
    if i % a == b and i % c == d:
        temp = i
        print(i, end=" ")
if temp == 0:
    print(-1)
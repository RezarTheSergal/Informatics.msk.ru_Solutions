n = int(input())
pivo = list(map(int, input().split()))

for i in range(n  -1, 0, -1):
    for j in range(i):
        if pivo[j] > pivo[j + 1]:
            pivo[j], pivo[j + 1] = pivo[j + 1] ,   pivo[j]
            print(*pivo)

if len(pivo) < 2:
    print(pivo[0])

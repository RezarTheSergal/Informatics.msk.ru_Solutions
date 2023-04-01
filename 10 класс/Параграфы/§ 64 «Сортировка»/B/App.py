N = int(input())
data = list(map(int, input().split()))

for j in range(0,3):
    imin = j
    for i in range(j+1, N):
        if data[i] < data[imin]:
            imin = i

    temp = data[imin]
    for i in range(imin, j, -1):
        data[i] = data[i - 1]
    data[j] = temp

print(*data)

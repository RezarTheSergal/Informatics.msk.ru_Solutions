N = int(input())
array = list(map(int, input().split()))

for i in range(0, N - 1, 2):
    temp = array[i]
    array[i] = array[i + 1]
    array[i + 1] = temp

print(*array)

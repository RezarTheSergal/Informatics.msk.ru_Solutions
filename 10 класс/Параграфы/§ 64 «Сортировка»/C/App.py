n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

unique_values = []
for num in arr:
    if num not in unique_values:
        unique_values.append(num)

print(*arr)
print(len(unique_values))

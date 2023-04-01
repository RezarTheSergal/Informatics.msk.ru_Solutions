number = int(input())
arr = list(map(int, input().split()))

print(*sorted(arr, key=lambda x: x%10), sep=" ")

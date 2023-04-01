from math import prod
n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

print(sum(arr), prod(arr))

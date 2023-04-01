from math import prod

n = int(input())
arr = []

while n:   
    arr.append(n)
    n = int(input())

print(sum(arr), prod(arr))

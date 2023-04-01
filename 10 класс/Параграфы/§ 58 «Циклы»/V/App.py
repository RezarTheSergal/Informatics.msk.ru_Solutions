n = int(input())
arr = []

while n:   
    arr.append(n)
    n = int(input())

print(min(arr), max(arr))

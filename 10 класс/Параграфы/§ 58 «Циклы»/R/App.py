n, x= map(int, input().split())
counter = 0
while n > 0 and x > 0:
    counter += 1
    if n > x:
        n -= x
    else:
        x -= n

print(x + n, counter)

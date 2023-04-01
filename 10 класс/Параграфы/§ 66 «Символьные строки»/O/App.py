a = input().split('.')
rash = input()
if len(a) > 1:
    a[len(a)-1] = rash
else:
    a.append(rash)

print(*a, sep='.')

a = input().split()
temp = a[0]
maxLen = len(a[0])
for i in a:
    if len(i) > maxLen:
        maxLen = len(i)
        temp = i
print(temp, maxLen, sep='\n')

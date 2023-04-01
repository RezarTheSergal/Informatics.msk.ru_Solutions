a = input()[::-1]
counter = 0
for i in range(len(a)):
    if a[i] == 'B':         
        counter = a[i:].count('R')
        a = a[:i] + a[i:].replace('R', '')
        break
      
print(a[::-1], counter, sep='\n')

a = input()
counter = 0
for i in range(len(a)):
    if a[i] == 'R':         
        counter = a[i:].count('B')
        a = a[:i] + a[i:].replace('B', '')
        break
      
print(a, counter, sep='\n')

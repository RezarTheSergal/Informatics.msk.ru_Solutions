a = input()
counter = 0
for i in a:
    if i == 'a':
        counter += 1
print(a.replace('a', 'b'), counter, sep='\n')

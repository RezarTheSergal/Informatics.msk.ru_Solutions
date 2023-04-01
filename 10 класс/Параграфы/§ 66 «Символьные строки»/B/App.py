a = input()
counter = 0
for i in a:
    if i == 'a' or i == 'A':
        counter += 1
print(a.replace('a', 'b').replace('A', 'B'), counter, sep='\n')

string = input().replace("+", " + ").replace("-", " - ")

splitted_string = string.split()
answ = int(splitted_string[0])

for i in range(1, len(splitted_string)-1):
    if splitted_string[i] == '+':
        answ += int(splitted_string[i+1])
    elif splitted_string[i] == '-':
        answ -= int(splitted_string[i+1])
      
print(answ)
    

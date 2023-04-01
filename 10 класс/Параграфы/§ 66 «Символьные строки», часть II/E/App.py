string = ""
temp = input()
while temp != "":
    string += " " + temp
    temp = input()
    
splitted_string = string.split()
array = list()
for i in range(len(splitted_string)):
    if i % 2 != 0:
        array.append(splitted_string[i])

array = sorted(array)
for i in range(len(array)):
    print(str(i+1) + '. ' + array[i])

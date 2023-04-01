number = int(input())

string = ""
for i in range(number):
    string += " " + input()
    
splitted_string = string.split()
array = list()
for i in range(len(splitted_string)):
    if i % 2 != 0:
        array.append(splitted_string[i])

array = sorted(array)
for i in range(len(array)):
    print(str(i+1) + '. ' + array[i])

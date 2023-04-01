import random as rd
num = int(input())
array = [i for i in range(1,num+1)]

for i in range(num):
    random = rd.randint(0,num-1)
    temp = array[i]
    array[i] = array[random]
    array[random] = temp

print(*array)
    

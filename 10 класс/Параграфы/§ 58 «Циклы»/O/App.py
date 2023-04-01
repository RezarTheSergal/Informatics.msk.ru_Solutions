number = int(input())
temp = number
check = False
arr = []

while temp:
    arr.append(temp % 10)
    temp //= 10

while number:
    counter = 0
    one_dig = number % 10
    
    for i in arr:
        if i == one_dig:
            counter += 1
    if counter >= 2:
        print("Yes")
        check = True
        break
    number //= 10

if not check:
    print("NO")
   

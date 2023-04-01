number = int(input())
temp_dig = number % 10
check = True

while number:
    if number % 10 != temp_dig:
        print("NO")
        check = False
        break
    number //= 10

if check:
    print("YES")
        

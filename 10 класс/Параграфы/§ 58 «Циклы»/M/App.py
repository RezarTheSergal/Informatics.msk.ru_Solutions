number = int(input())
prev_dig = 0
this_dig = 0
check = False
while number:
    this_dig = number % 10

    if prev_dig == this_dig:
        print("YES")
        check = True
        break
    prev_dig = this_dig
    number //= 10

if not check:
    print("NO")

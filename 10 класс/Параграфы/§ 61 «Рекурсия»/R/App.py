def SimpleDivisors(number, move = 2):  
    if number > 1:
        if number % move == 0:
            print(int(move), end=' ')
            SimpleDivisors(number / move)
        else:
            if IsSimple(number) and number > 1000:
                 print(int(number), end=' ')
                 number /= number
            else:
                SimpleDivisors(number, move + 1)
            

def IsSimple(num, itterator = 2):
    if num < itterator**2:
        return True
    if num % itterator == 0:
        return False
    return IsSimple(num, itterator + 1)

number = int(input())

if number <= 1:
    print(int(number))
else:
    SimpleDivisors(number)

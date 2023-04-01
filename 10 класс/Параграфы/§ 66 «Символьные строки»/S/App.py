def convertation(number, base):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result

def negativeOrNot(strNum, is_negative):
    if is_negative:
        return '-' + strNum
    else:
        return strNum

a = input()
bases = input().split()

negative = False
if a[0] == '-':
    negative = True
    
a = abs(int(a, int(bases[0])))

print(negativeOrNot(convertation(a, int(bases[1])), negative))

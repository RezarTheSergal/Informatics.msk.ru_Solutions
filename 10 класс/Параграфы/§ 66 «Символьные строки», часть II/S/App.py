import math

def add_three_digits(number):
    return f"{number:.3f}"

def equation_roots(a, b, c):
    discriminant = math.pow(b, 2) - (4*a*c)
    first = -4294967296
    second = -4294967296
    if discriminant > 0:
        root = math.sqrt(discriminant)
        first = add_three_digits((-b + root) / (2*a))
        second = add_three_digits((-b - root) / (2*a))
        return [first, second] if float(first) < float(second) else [second, first]
    elif discriminant == 0:
        first = add_three_digits(-b / (2*a))
        return [first]

def find_number(equation):
    array = equation.replace("-", " -").replace("+", " +").split()
    a = ''
    b = ''
    c = ''
    for s in array:
        if s.find('a') != -1:
            a = s[:s.find('a')]
            if a == '+' or a == '':
                a = '1'
            elif a == '-':
                a = '-1'
        elif s.find('b') != -1:
            b = s[:s.find('b')]
            if b == '+' or b == '':
                b = '1'
            elif b == '-':
                b = '-1'
        else:
            c = s
    
    return [float(a), float(b), float(c)]

equation = input()
coefs = find_number(equation)
print(*equation_roots(*coefs))

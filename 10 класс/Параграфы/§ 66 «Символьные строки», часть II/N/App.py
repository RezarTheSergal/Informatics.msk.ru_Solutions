s = input()
array = list()
for ch in s:
    if ch.isdigit():
        array.append(int(ch))

print(*sorted(array)[::-1], sep='')

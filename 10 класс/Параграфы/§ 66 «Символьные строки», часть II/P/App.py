data = input()
freqs = [0] * 10
for ch in data:
    if ch.isdigit():
        freqs[ord(ch) - ord('0')] += 1

pal = ''
center = ('' if freqs[0]%2 == 0 else '0')

for i in range(9, -1, -1):
    if freqs[i] % 2:
        center = str(i)
        freqs[i] -= 1
        
for i in range(1, 10):
    pal += str(i) * (freqs[i] // 2)

pal0 = '0' * (freqs[0] // 2)

if len(pal) > 0:
    pal = pal[0] + pal0 + (pal[1:] if len(pal) > 1 else '')
    pal = pal + center + pal[::-1]
else:
     pal = (center if freqs[0] == 0 else '0')

print(pal)

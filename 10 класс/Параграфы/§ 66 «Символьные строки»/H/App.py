a = input()
length = len(a)
b = a[0:length//2]
c = a[length//2:]
if length %2:
    c = a[length//2+1:]

print("YES" if b == c[::-1]else "NO")

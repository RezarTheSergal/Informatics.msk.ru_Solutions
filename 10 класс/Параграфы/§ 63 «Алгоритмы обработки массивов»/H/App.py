N = int(input())
array = list(map(int, input().split()))

mlen, clen, number = 1, 1, array[0]
for i in range(1, N):
    if array[i] == array[i-1]:
        clen += 1
        if clen > mlen:
            mlen = clen
            number = array[i]
    else:
        clen = 1
print(number, mlen)

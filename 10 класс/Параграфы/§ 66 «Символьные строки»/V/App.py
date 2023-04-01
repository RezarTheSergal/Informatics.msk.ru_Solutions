alphavit = input()
wordlen = int(input())

power = len(alphavit)
for num in range(power ** wordlen):
    word = ' '
    for p in range(wordlen):
        word = alphavit[num // (power ** p) % power] + word
    print(word)
print(power ** wordlen)

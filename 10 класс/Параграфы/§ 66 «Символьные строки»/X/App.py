alphavit = input()
wordlen = int(input())

power = len(alphavit)
c = 0
for num in range(power ** wordlen):
    word = ' '
    for p in range(wordlen):
        word = alphavit[num // (power ** p) % power] + word
    if word.count(alphavit[0]) > 1:
        print(word)
        c += 1
print(c)

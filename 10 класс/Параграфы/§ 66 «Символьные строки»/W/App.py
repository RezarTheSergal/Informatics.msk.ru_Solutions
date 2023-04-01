alphavit = input()
wordlen = int(input())
power = len(alphavit)

for num in range(power ** (wordlen - 1)):
    word = ""
    for p in range(wordlen-1):
        word = alphavit[num // (power ** p) % power] + word
    print(word[0] + alphavit[0] + word[1:])
print(power ** (wordlen - 1))

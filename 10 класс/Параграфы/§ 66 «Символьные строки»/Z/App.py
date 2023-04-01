alphavit = input()
wordlen = int(input())

power = len(alphavit)
c = 0
for num in range(power ** wordlen):
    word = ' '
    for p in range(wordlen):
        word = alphavit[num // (power ** p) % power] + word
    valid_word = True
    for i in range(len(alphavit)):
        if word.count(alphavit[i]) < 2:
            valid_word = False
        else:
            valid_word = True
            break
    if valid_word:
        print(word)
        c += 1
print(c)

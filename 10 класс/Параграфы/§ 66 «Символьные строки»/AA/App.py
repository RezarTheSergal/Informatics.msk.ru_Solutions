alphavit = input()
wordlen = int(input())
dict = "AEIOU"
power = len(alphavit)
c = 0
for num in range(power ** wordlen):
    word = ""
    for p in range(wordlen):
        word = alphavit[num // (power ** p) % power] + word
    valid_word = True
    for i in range(len(word) - 1):
        if word[i] in dict and word[i + 1] in dict:
            valid_word = False
    if valid_word:
        print(word)
        c += 1
print(c)

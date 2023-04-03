def shift_letter(letter, shift):
    if letter.isalpha():
        delta = ord('A') if letter.isupper() else ord('a')
        return chr((ord(letter) - delta + shift) % 26 +delta)
    else:
        return letter

def encode_words(text):
    words = []
    word = ''
    for ch in text:
        if ch.isalpha():
            word += ch
        else:
            words.append(word)
            word = ''
    words.append(word)
    encrypted_words = []
    for word in words:
        shift = len(word)
        encrypted_word = ''
        for letter in word:
            encrypted_word += shift_letter(letter, shift)
        encrypted_words.append(encrypted_word)
    result = ''
    i = 0
    for ch in text:
        if ch.isalpha():
            result += encrypted_words[i][0]
            encrypted_words[i] = encrypted_words[i][1:]
        else:
            result += ch
        if i < len(encrypted_words) - 1 and not encrypted_words[i].isalpha():
            i += 1
    return result

text = input()
encrypted_text = encode_words(text)
print(encrypted_text)

def clear_input(s):
    result = ""
    for ch in s:
        if ch.isalpha() and ch != ' ':
            result += ch.upper()
    return result


s = clear_input(input())
s = sorted(s, key=lambda x:s.count(x))[::-1]

temp = ""
for i in range(len(s)):
    if s[i] not in temp:
        temp += s[i]

counter = 0
middle_char = ''
temp_char_usage_couner = [0] * len(temp)
middle_char_flag = False
is_bullshit = False
i = 0
for ch in temp:
    temp_char_usage_couner[i] = s.count(ch)
    i += 1
    if s.count(ch) % 2 != 0:
        middle_char = ch
        middle_char_flag = True
        counter += 1
    if counter > 1:
        print("NO")
        is_bullshit = True
        break

if not is_bullshit:
    result = ""
    for i in range(len(temp)):
        for _ in range(temp_char_usage_couner[i] // 2):
            result += temp[i]

    answer = ""
    for ch in sorted(result):
        answer += ch
        
    result = answer

    print(result[::-1] + middle_char + result if middle_char_flag else result[::-1] + result )

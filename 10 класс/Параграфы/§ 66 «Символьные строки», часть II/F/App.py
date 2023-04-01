def compare(item):
    return item.split()[1]

families = []
temp = input()
while temp != "":
    families.append(temp)
    temp = input()

families.sort(key=compare)

for i in range(1, len(families) + 1):
    print(str(i) + '. ', families[i-1])

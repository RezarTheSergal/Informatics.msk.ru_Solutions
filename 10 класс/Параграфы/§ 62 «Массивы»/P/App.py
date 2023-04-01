import random as rnd

start, end, num = map(int, input().split())
array = [rnd.randint(start, end) for i in range(num)]

averageBelow = 0.0
counterBelow = 0
averageHigher = 0.0
counterHigher = 0
for i in array:
    if i >= 50:
        averageHigher+=i
        counterHigher+=1
    else:
        averageBelow+=i
        counterBelow+=1
        
print(*array)

if counterBelow != 0:
    print("%.3f" % (averageBelow / counterBelow), end=" ")
else:
    print("0.000")

if counterHigher != 0:
    print("%.3f" % (averageHigher / counterHigher), end=" ")
else:
    print("0.000")

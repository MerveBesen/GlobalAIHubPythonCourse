import random as rnd

randomList = []
newList = []

for i in range (30):
    randomList.append(rnd.randrange(1,100))

print(randomList)

newList = (randomList[15::] + randomList[:15:])
print(newList)

n = int(input("Please enter a single digit integer : "))

a=0
for i in newList:
    a += 1
    if i%2 == 0 :
        print(i)

    if a == n:
        break

    else :
        pass
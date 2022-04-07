randList = [0,9,6,4,-1,3,-5,1,7]

for i in range(len(randList)):
    for j in range(i + 1, len(randList)):

        if randList[i] > randList[j]:
            randList[i], randList[j] = randList[j], randList[i]

print(randList)
num = int(input())
numList = list(map(int, input().split()))

demicalNum = 0

for i in range(num):
    for j in range(2,1000):
        if numList[i] % j == 0:
            if numList[i] == j:
                demicalNum = demicalNum + 1 #합성수 아님                
            break #합성수임 

print(demicalNum)


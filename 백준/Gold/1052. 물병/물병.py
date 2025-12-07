
N, K = map(int, input().split())
check = N
bitList = []
while True:
    b = check % 2 
    a = check // 2
    if a == 0:
        bitList.append(b)
        break
    else:
        bitList.append(b)
        check = a

answer = 0
while True:
    temp = 0
    for i in range(len(bitList)):
        if(bitList[i] == 1):
            temp += 1
    if temp <= K:
        break
    answer += 1

    bitList[0] += 1
    for i in range(len(bitList)):
        if(bitList[i] == 2):
            bitList[i] = 0
            if i == len(bitList) - 1:
                bitList.append(1)
            else:
                bitList[i+1] += 1
        
    
print(answer)
    
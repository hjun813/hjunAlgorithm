N, K = map(int, input().split())
diff = []
for i in range(N):
    A, B = map(int, input().split())
    if A-B > 0:
        diff.append(0)
    else:
        diff.append(-A+B)

answer = 0
temp = 0
for i in range(N):
    if diff[i] == 0:
        temp += 1

if temp >= K:
    print(answer)
else:
    dif = K - temp
    check = 0
    diff.sort()

    for i in range(N):
        
        if diff[i] == 0:
            continue
        else:
            check += 1
            if check == dif:
                answer = diff[i]
                break
            
    print(answer)
    

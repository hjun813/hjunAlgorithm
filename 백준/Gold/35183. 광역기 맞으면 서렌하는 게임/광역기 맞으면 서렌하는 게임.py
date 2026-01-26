N = int(input())
attack = []
answer = "Surrender"
safe = [[0 for _ in range(1001)] for _ in range(N)]

for i in range(N):
    L, R = map(int, input().split())
    attack.append([L,R]) 

if N == 1:
    answer = "World Champion"
else:
    for i in range(N):
        left = attack[i][0]
        right = attack[i][1]
        if i == 0:
            for j in range(1001):
                if left <= j <= right:
                    continue
                else:
                    safe[i][j] += 1
        else:            
            for j in range(1001):
                if left <= j <= right:
                    if j == 0:
                        safe[i][j] = min(safe[i-1][j], safe[i-1][j+1])
                    elif j == 1000:
                        safe[i][j] = min(safe[i-1][j-1], safe[i-1][j])
                    else:
                        safe[i][j] = min(safe[i-1][j-1], safe[i-1][j], safe[i-1][j+1])
                    
                else:
                    if j == 0:
                        safe[i][j] = min(safe[i-1][j], safe[i-1][j+1]) + 1
                    elif j == 1000:
                        safe[i][j] = min(safe[i-1][j-1], safe[i-1][j]) + 1
                    else:
                        safe[i][j] = min(safe[i-1][j-1], safe[i-1][j], safe[i-1][j+1]) + 1
                
    for k in range(1, 1001):
        if safe[-1][k] <= 1:
            answer = "World Champion"
            break

    # for i in range(N):
    #     print(safe[i])
print(answer)
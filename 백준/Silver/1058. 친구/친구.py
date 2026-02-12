N = int(input())
info = []
checkInfo = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

for i in range(N):
    temp = list(input().strip())
    info.append(temp)

for i in range(N):
    for j in range(N):
        if info[i][j] == 'Y':
            checkInfo[i][j] = 1
            # 여기서 j의 친구도 내친구
            for k in range(N):
                if info[j][k] == 'Y':
                    checkInfo[i][k] = 1

for i in range(N):
    answer = max(answer, sum(checkInfo[i]) - 1)

print(answer)
            
from collections import deque
N, M = map(int, input().split())
mapInfo = []

for i in range(M):
    temp = list(map(int, input().split()))
    mapInfo.append(temp)

answer = "No"

dir = [[0,1], [1,0]]

visit = [[0 for _ in range(N)] for _ in range(M)]
visit[0][0] = 1

check = deque([])
check.append([0,0])

while check:
    a, b = check.popleft()

    if a == M-1 and b == N-1:
        answer = "Yes"
        break
        
    for i in range(2):
        if 0 <= a + dir[i][0] and a + dir[i][0] < M and 0 <= b + dir[i][1] and b + dir[i][1] < N:
            if mapInfo[a + dir[i][0]][b + dir[i][1]] == 1:
                if visit[a + dir[i][0]][b + dir[i][1]] == 0:
                    visit[a + dir[i][0]][b + dir[i][1]] = 1
                    check.append([a + dir[i][0], b + dir[i][1]])
            
print(answer)
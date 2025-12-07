from collections import deque
N, M, K = map(int, input().split())
mapInfo = []
for i in range(N):
    temp = list(map(int, input().split()))
    mapInfo.append(temp)

dir1 = [[0,1], [1,0], [0,-1], [-1,0]]
group = []

answer = 0
answer2 = "IMPOSSIBLE"
visit = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if mapInfo[i][j] == 0:
            if visit[i][j] == 0:
                tempQ = deque([])
                tempSize = 0
                tempQ.append([i,j])
                visit[i][j] = 1
                while tempQ:
                    a, b = tempQ.pop()
                    tempSize += 1
                    for k in range(4):
                        n_a = a + dir1[k][0]
                        n_b = b + dir1[k][1]
                        if 0<=n_a<N and 0<=n_b<N:
                            if mapInfo[n_a][n_b] == 0:
                                if visit[n_a][n_b] == 0:
                                    visit[n_a][n_b] = 1
                                    tempQ.append([n_a, n_b])
                group.append(tempSize)

for i in range(len(group)):
    s = group[i]
    remain = s % K
    need = s // K
    if remain != 0:
        need += 1
    answer += need
if answer== 0:
    print(answer2)
elif answer <= M:
    answer2 = "POSSIBLE"
    print(answer2)
    print(M-answer)
else:
    print(answer2)
                    
N, M = map(int, input().split())
mapInfo = []
dir = [[0,1],[0,-1],[1,0],[-1,0]]
answer = 0
visited = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    temp = list(map(int, input().split()))
    mapInfo.append(temp)

# 4개짜리 하나만 두는 거구나
# 백트래킹으로 해야하는거 같은데

def tertromino(n, a, b, visit, sumN): # (a,b) n번째 재귀
    global answer
    if n == 4:
        answer = max(sumN, answer)
        return
    
    for i in range(4):
        if 0 <= a + dir[i][0] < N and 0 <= b + dir[i][1] < M:
            if visit[a + dir[i][0]][b + dir[i][1]] == 0:
                visit[a + dir[i][0]][b + dir[i][1]] = 1
                newSum = mapInfo[a + dir[i][0]][b + dir[i][1]] + sumN
                tertromino(n+1, a + dir[i][0], b + dir[i][1], visit, newSum)
                visit[a + dir[i][0]][b + dir[i][1]] = 0

def tertromino2(a, b):
    global answer
    
    for i in range(4):
        n = 1
        temp = mapInfo[a][b]
        for j in range(4):
            if i != j:
                if 0 <= a + dir[j][0] < N and 0 <= b + dir[j][1] < M:
                    n += 1
                    temp += mapInfo[a + dir[j][0]][b + dir[j][1]]
        if n == 4:
            answer = max(answer, temp)

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        total = mapInfo[i][j] 
        tertromino(1, i, j, visited, total)
        tertromino2(i, j)
        visited[i][j] = 0

print(answer)
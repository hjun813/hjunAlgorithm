mapInfo = []
for i in range(5):
    temp = list(map(int, input().split()))
    mapInfo.append(temp)
r, c = map(int, input().split())
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
answer = 26

def mazeRunner(n, a, b, changedMap, m):
    global answer
    if n == 3:
        answer = min(answer, m)
        return
        
    for i in range(4):
        nx = a + dir[i][0]
        ny = b + dir[i][1]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if changedMap[nx][ny] == 0:
                changedMap[nx][ny] = -1
                mazeRunner(n, nx, ny, changedMap, m+1)
                changedMap[nx][ny] = 0
            elif changedMap[nx][ny] == 1:
                n += 1
                changedMap[nx][ny] = -1
                mazeRunner(n, nx, ny, changedMap, m+1)
                changedMap[nx][ny] = 1
                n -= 1


mapInfo[r][c] = -1
mazeRunner(0, r, c, mapInfo, 0)

if answer == 26:
    print(-1)
else:
    print(answer)
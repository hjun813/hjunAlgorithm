from collections import deque
n, m = map(int, input().split())
paint = []
dir = [[-1,0], [1,0], [0,1], [0,-1]]

for i in range(n):
    row = list(map(int, input().split()))
    paint.append(row)

paintNum = 0
maxSize = 0
visit = [[0 for _ in range(m)] for _ in range(n)]
check = deque([])

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and visit[i][j] == 0:
            check.append([i,j])
            visit[i][j] = 1
            tempSize = 1
            while check:
                x, y = check.pop()
                for k in range(4):
                    n_x = x + dir[k][0]
                    n_y = y + dir[k][1]
                    if 0<= n_x < n and 0<= n_y < m:
                        if paint[n_x][n_y] == 1 and visit[n_x][n_y] == 0:
                            check.append([n_x, n_y])
                            visit[n_x][n_y] = 1
                            tempSize += 1
            maxSize = max(maxSize, tempSize)
            paintNum += 1

print(paintNum)
print(maxSize)
            
            
            
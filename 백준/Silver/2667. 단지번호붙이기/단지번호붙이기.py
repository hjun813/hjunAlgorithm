import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
count = 0
townmap = []
apart = []

for i in range(N):
    townmap.append(list(map(str, input().strip())))

visited = [[False for _ in range(N)] for _ in range(N)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
    queue = deque([(i,j)])
    num = 1
    while queue:
        k = queue.popleft()
        x,y = k
        visited[x][y] = True
        for a,b in direction:
            if 0<=x+a<N and 0<=y+b<N:
                if townmap[x+a][y+b] == '1':
                    if not visited[x+a][y+b]:
                        queue.append((x+a, y+b))
                        visited[x+a][y+b] = True
                        num += 1
    return num

for i in range(N):
    for j in range(N):
        if townmap[i][j] == '1':
            if not visited[i][j]:
                apart.append(bfs(i,j))
                count += 1

apart.sort()
print(count)
for i in range(len(apart)):
    print(apart[i])

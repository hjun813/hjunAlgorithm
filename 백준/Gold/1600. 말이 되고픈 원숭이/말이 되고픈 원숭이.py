from collections import deque
K = int(input())
W, H = map(int, input().split())
mapInfo = []
visited = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(K+1)]

answer = -1

for i in range(H):
    temp = list(map(int, input().split()))
    mapInfo.append(temp)

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
horseDir = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

monkey = deque([])
monkey.append([0, 0, 0, 0])

while monkey:
    n, a, b, k = monkey.popleft()

    if a == H -1 and b == W - 1:
        answer = n
        break

    # 일반 이동
    for i in range(4):
        x, y = dir[i]
        if 0 <= x+a < H and 0 <= y+b < W:
            if visited[k][x+a][y+b] == 0:
                if mapInfo[x+a][y+b] == 0:
                    visited[k][x+a][y+b] = 1
                    monkey.append([n+1, x+a, y+b, k])
    # 말점프
    if k + 1 <= K:
        for x, y in horseDir:
            if 0 <= x + a < H and 0 <= y+b < W:
                if visited[k+1][x+a][y+b] == 0:
                    if mapInfo[x+a][y+b] == 0:
                        visited[k+1][x+a][y+b] = 1
                        monkey.append([n+1, x+a, y+b, k+1])
    
    

print(answer)
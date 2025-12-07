from collections import deque

dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_y = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(landCheck, visit, mapInfo):
    while landCheck:
        a, b = landCheck.pop()
        for i in range(8):
            n_x = a + dir_x[i]
            n_y = b + dir_y[i]
            if 0<=n_x<h and 0<=n_y<w:
                if mapInfo[n_x][n_y] == 1:
                    if visit[n_x][n_y] == 0:
                        visit[n_x][n_y] = 1
                        landCheck.append([n_x, n_y])
                        


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapInfo = []
    landCheck = []
    visit = [[0 for _ in range(w)]for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        mapInfo.append(list(map(int, input().split())))

    for j in range(h):
        for i in range(w):
            if mapInfo[j][i] == 1:
                if visit[j][i] == 0:
                    landCheck.append([j, i])
                    bfs(landCheck, visit, mapInfo)
                    cnt += 1
                    
    print(cnt)


    
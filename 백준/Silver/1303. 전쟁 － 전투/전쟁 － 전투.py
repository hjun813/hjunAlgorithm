import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
direction = [[0,1], [0,-1], [1,0], [-1,0]]
white = 0
blue = 0

mapInfo = [[0 for _ in range(N)] for _ in range(M)]
visited = [[0 for _ in range(N)] for _ in range(M)]

for i in range(M):
    
    mapstr = list(map(str, input()))
    for j in range(N):
        if(mapstr[j] == "W"):
            mapInfo[i][j] = 1
       
def fun(i, j, f):
    global cnt
    if mapInfo[i][j] == f:
        cnt += 1
        mapInfo[i][j] = -1
        visited[i][j] = 1
        for a,b in direction:
            if 0<=i+a< M and 0<=j+b<N :
                if mapInfo[i+a][j+b] == f:
                    if visited[i+a][j+b] == 0:
                        fun(i+a, j+b, f)

            
for i in range(M):
    for j in range(N):
        if mapInfo[i][j] == -1:
            continue
        elif(mapInfo[i][j] == 1):
            cnt = 0
            fun(i, j, 1)
            white += cnt**2
            
        elif(mapInfo[i][j] == 0):
            cnt = 0
            fun(i, j, 0)
            blue += cnt**2

print(white, blue)
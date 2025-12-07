import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [[False for _ in range(M)] for _ in range(N)]
floor = []
hor = 0
ver = 0

for i in range(N):
    floor.append(list(map(str, input().strip())))

def checkhor(a,b): #a,b 는 좌표
    if not visited[a][b]:
        if floor[a][b] == '-':
            if 0<=b+1<M:
                if not visited[a][b+1]:
                    if floor[a][b+1] == '-':
                        checkhor(a, b+1)
                        visited[a][b+1] = True

def checkver(a,b): #a,b 는 좌표

    if not visited[a][b]:
        if floor[a][b] == '|':
            if 0<=a+1<N:
                if not visited[a+1][b]:
                    if floor[a+1][b] == '|':
                        checkver(a+1, b)
                        visited[a+1][b] = True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
               
            if floor[i][j] == '-':
                checkhor(i,j)
         
                hor += 1
                visited[i][j] = True
            elif floor[i][j] == '|':
                checkver(i,j)
         
                ver += 1
                visited[i][j] = True

print(hor + ver)
N, M = map(int, input().split())
mapInfo = []

for i in range(N):
    info = list(map(int, input().split()))
    mapInfo.append(info)

# 강화 유리 1, 일반 유리 0

dir = [[1, -1], [1, 0], [1, 1]]
cnt = 0
maphack = [[0 for _ in range (M)] for _ in range (N)]
for i in range(M):
    if mapInfo[0][i] == 1:
        maphack[0][i] = 1

for i in range(1, N):
    for j in range(M):
        if mapInfo[i][j] == 1:
            for k in range(-1, 2):
                if 0<=i-1 and 0<=j+k<M:
                    if maphack[i-1][j+k] != 0:
                        maphack[i][j] += maphack[i-1][j+k]

for i in range(M):
    cnt += maphack[-1][i]

print(cnt % 1000000007)
    


    
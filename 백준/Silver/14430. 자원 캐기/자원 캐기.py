N, M = map(int, input().split())

mapInfo = []

for i in range(N):
    temp = list(map(int, input().split()))
    mapInfo.append(temp)

dir = [[0,1],[1,0]]

dp = [[0 for _ in range(M + 1)]for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        temp = max(dp[i-1][j], dp[i][j-1])
        if mapInfo[i-1][j-1] == 1:
            dp[i][j] = temp + 1
        else:
            dp[i][j] = temp
            
print(dp[N][M])
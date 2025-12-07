N, D = map(int, input().split())
roadInfo = []
dp = [i for i in range(D+1)]

for i in range(N):
    s, e, d = map(int, input().split())
    if e > D:
        continue
    if e - s > d:
        roadInfo.append([s,e,d])

roadInfo.sort()

# for i in range(len(roadInfo)):
#     S = roadInfo[i][0]
#     E = roadInfo[i][1]
#     L = roadInfo[i][2]

#     dp[E] = min(dp[E], dp[S] + L)

for i in range(1, D+1):
    for j in range(len(roadInfo)):
        S = roadInfo[j][0]
        E = roadInfo[j][1]
        L = roadInfo[j][2]
        if i == E:
            dp[i] = min(dp[i], dp[i-1] + 1, dp[S] + L)
    dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[-1])
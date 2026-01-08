n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
    
# 마시면 다 마시고 빈컵 원상복귀
# 3개 연속으로는 못먹음
# n 번째 상황이라 생각
# 이전까지 0개 먹었을 때 최대
# 이전까지 1개 먹었을 때 최대
# 이전까지 2개 먹었을 때 최대

dp = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i][1] = wine[i]
    
    else:
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = dp[i-1][0]+ wine[i]
        dp[i][2] = dp[i-1][1] + wine[i]

print(max(dp[-1][0], dp[-1][1], dp[-1][2]))
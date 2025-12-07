import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+5)]

# dp[i] 가 i원 일때 거스름돈 최소 개수
# dp[i] = min(dp[i-5] + 1, dp[i-2] + 1)
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 2
dp[5] = 1

if n > 5:
    for i in range(6, n+2):
        if dp[i-5] != 0 and dp[i-2] != 0:
            dp[i] = min(dp[i-5] + 1, dp[i-2] + 1)
        elif dp[i-5] == 0 and dp[i-2] != 0:
            dp[i] = dp[i-2] + 1
        elif dp[i-5] != 0 and dp[i-2] == 0:
            dp[i] = dp[i-5] + 1
        elif dp[i-5] == 0 and dp[i-2] == 0:
            dp[i] = 0

# print(dp)
if dp[-5] != 0:
    print(dp[-5])
else:
    print(-1)
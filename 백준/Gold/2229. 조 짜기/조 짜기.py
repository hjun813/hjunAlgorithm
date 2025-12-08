N = int(input())
studentScore = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(N+1):
    if i == 0 or i == 1:
        dp[i] = 0
    else:
        for j in range(i):
            maxT = max(studentScore[j:i:])
            minT = min(studentScore[j:i:])
            dp[i] = max(dp[i], dp[j] + maxT - minT)
print(dp[-1])
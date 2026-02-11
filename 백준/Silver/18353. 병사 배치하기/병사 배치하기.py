N = int(input())
soldier = list(map(int, input().split()))
dp = [1 for _ in range(N)]

# i번째 포함 가장 긴 조합따지려면

dp[0] = 1

for i in range(1, N):
    for j in range(0, i):
        if soldier[i] < soldier[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
        

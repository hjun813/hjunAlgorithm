import sys
input = sys.stdin.readline

n = int(input())
get = list(map(int, input().split()))

# i 번째 최대
# i 번째가 포함 되냐 안되냐

dp = [0 for _ in range(n)]
dp[0] = get[0]
for i in range(1, n):
    dp[i] = max(dp[i-1] + get[i], get[i])

print(max(dp))
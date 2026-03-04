N = int(input())
red = []
green = []
blue = []

for i in range(N):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)

# i 번째의 최소

dp = [[0 for _ in range(3)] for _ in range(N)]
dp[0][0] = red[0]
dp[0][1] = green[0]
dp[0][2] = blue[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + red[i]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + green[i]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + blue[i]

print(min(dp[-1]))
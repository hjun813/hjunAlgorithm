N = int(input())
food = []

for i in range(N):
    food.append(int(input()))

# i번째 최대, 연속으로 0개, 1개, 2개 먹었을 때
# dp[i]

dp = [[0 for _ in range(3)] for _ in range(N)]

dp[0][1] =  food[0]

for i in range(1, N):
    
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + food[i]
    dp[i][2] = dp[i-1][1] + (food[i] // 2)

print(max(dp[-1]))
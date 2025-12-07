import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    sticker1 = list(map(int, input().split()))
    sticker2 = list(map(int, input().split()))
    dp = [[0 for _ in range(n)] for _ in range(2)]
   
    for i in range(n):
        
        if i == 0:
            dp[0][i] = sticker1[i] 
            dp[1][i] = sticker2[i]
        elif i == 1:
            dp[0][i] = dp[1][i-1] + sticker1[i]
            dp[1][i] = dp[0][i-1] + sticker2[i]
        else:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker1[i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker2[i]

    print(max(dp[0][-1], dp[1][-1]))
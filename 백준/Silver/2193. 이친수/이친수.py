N = int(input())
dp = [0 for _ in range(N)]

if N == 1 :
    print(1)
elif N == 2:
    print(1)
else:
    # 앞에가 무조건 10~이렇게 되어야 함
    dp[0] = 1
    dp[1] = 1
    # N == 1, (1)
    # N == 2, (10)
    # N == 3, (100, 101)
    # N == 4, (1000, 1001, 1010)
    # N == 5, (10000, 10001, 10010, 10100, 10101)
    # N - 2 까지의 합 + 1
    for i in range(2, N):
        # dp[i] = dp[0] ~ dp[i-2] 합
        for j in range(i-1):
            dp[i] += dp[j]
        dp[i] += 1
    print(dp[-1])


import sys
input = sys.stdin.readline
n = int(input())
dp = [-1] * (n+1)

def fibo(n):

    if dp[n] == -1:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

dp[0] = 0
dp[1] = 1
print(fibo(n))
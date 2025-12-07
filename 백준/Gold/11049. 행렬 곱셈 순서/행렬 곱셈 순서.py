import sys

input = sys.stdin.readline

N = int(input())
matrix = []
p = []

for _ in range(N):
    col, row = map(int, input().split())
    matrix.append((col, row))

p.append(matrix[0][0])

for r, c in matrix:
    p.append(c)

dp = [[0] * N for _ in range(N)]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = float("inf")
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            dp[i][j] = min(dp[i][j], cost)
            # print(dp)
            # print()

print(dp[0][N - 1])

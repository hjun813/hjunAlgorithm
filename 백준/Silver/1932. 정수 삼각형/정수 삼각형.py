import sys
input = sys.stdin.readline

n = int(input())
intTri = []

for _ in range(n):
    intTri.append(list(map(int, input().split())))


dp = [[0 for _ in range(n+1)] for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if i == 0:
            dp[i][j+1] = intTri[i][j]
        else:
            dp[i][j+1] = max(dp[i-1][j], dp[i-1][j+1]) + intTri[i][j]

print(max(dp[-1]))
import sys
input = sys.stdin.readline

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dp = [[0 for _ in range(N)] for _ in range(N)] # i, j 까지의 경로 수

# 생각하는 점화식
# dp[i][j] =
# dp[i][k] (0<k<j)중 k+graph[i][k] 가 j 인 애들 다더하고
# dp[k][j] (0<k<i)중 k+graph[k][j] 가 i 인 애들 다더하고

dp[0][0] = 1

for i in range(N):
    for j in range(N):

        # for p in range(N):
        #     print(dp[p])
        # print()


        for k in range(N-1):
            if k + graph[i][k] == j:
                # print(i, j ,k,"왼")
                dp[i][j] += dp[i][k]
        for k in range(N-1):
            if k + graph[k][j] == i:
                # print(i, j ,k, "위")
                dp[i][j] += dp[k][j]
# for p in range(N):
#     print(dp[p])

print(dp[-1][-1])
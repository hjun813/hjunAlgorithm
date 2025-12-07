import sys

N = int(input())
rows = N
cols = N
cost = [[0 for j in range(cols)] for i in range(rows)]
visited = [False] * N
minCost = float("inf")

for i in range(N):
    cost[i] = list(map(int, sys.stdin.readline().rstrip().split()))


def tripTo(depth, now, nowCost, start):
    global minCost

    if nowCost >= minCost:
        return

    if depth == N - 1:
        if cost[now][start] > 0:
            minCost = min(minCost, nowCost + cost[now][start])
        return

    for i in range(N):
        if not visited[i] and cost[now][i] > 0:
            visited[i] = True
            tripTo(depth + 1, i, nowCost + cost[now][i], start)
            visited[i] = False

visited[0]=True
tripTo(0, 0, 0, 0)
visited[0]=False

print(minCost)
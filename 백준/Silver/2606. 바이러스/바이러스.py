import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {i: [] for i in range(N + 1)}
visited = [False] * (N+1)
result = []

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in graph:
    graph[i].sort()

# print(graph)

def dfs(v):
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(len(result) - 1)

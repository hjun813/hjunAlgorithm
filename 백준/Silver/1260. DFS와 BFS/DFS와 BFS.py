import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

tree = {i : [] for i in range(N + 1)}
visitedDfs = [False] * (N+1)
resultDfs = []
visitedBfs = [False] * (N+1)
resultBfs = []

for _ in range(M):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for i in tree:
    tree[i].sort()
    
# print(tree)

def dfs(v):
    visitedDfs[v] = True
    resultDfs.append(v)
    for i in tree[v]:
        if not visitedDfs[i]:
            dfs(i)

dfs(V)
print(*resultDfs)


def bfs(v):
    queue = deque([v])
    visitedBfs[v] = True
    while queue:
        k = queue.popleft()
        resultBfs.append(k)
        for i in tree[k]:
            if not visitedBfs[i]:
                queue.append(i)
                visitedBfs[i] = True

bfs(V)
print(*resultBfs)
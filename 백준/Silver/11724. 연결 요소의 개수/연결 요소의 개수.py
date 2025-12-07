import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree = {i: [] for i in range(N + 1)}
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for i in tree:
    tree[i].sort()

# print(tree)

def connected(v):
    visited[v] = True

    for i in tree[v]:
        if not visited[i]:
            connected(i)
            visited[i] = True

for i in range(1, N + 1):
    if not visited[i]:
        connected(i)
        count += 1

print(count)
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

V, E = map(int, input().split())
edge = []
total = 0

for _ in range(E):
    a, b, weight = map(int, input().split())
    edge.append((weight, a, b))

edge.sort()
parent = [0] * (V + 1)

for i in range(V + 1):
    parent[i] = i


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b):
    parent_a = find(parent, a)
    parent_b = find(parent, b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


for i in range(E):
    cost, a, b = edge[i]

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total += cost

print(total)
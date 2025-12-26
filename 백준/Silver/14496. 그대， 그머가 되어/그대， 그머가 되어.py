from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())
dic_h = {i : [] for i in range(1, N+1)}
visited = [0 for _ in range(N)]
answer = 0

for i in range(M):
    x, y = map(int, input().split())
    if x == y:
        continue
    dic_h[x].append(y)
    dic_h[y].append(x)
    
que = deque([])

for i in dic_h[a]:
    que.append([i, 1])
    visited[i-1] = 1
visited[a-1] = 1

while que:
    next, n = que.popleft()
    if next == b:
        answer = n
        break
    else:
        for i in dic_h[next]:
            if visited[i-1] == 0:
                que.append([i, n+1])
                visited[i-1] = 1
if a == b:
    print(0)
else:
    if answer == 0:
        print(-1)
    else:
        print(answer)

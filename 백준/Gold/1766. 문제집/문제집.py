import sys
import heapq
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {i : [] for i in range(1,N+1)}
indegree = [0 for _ in range(N+1)]
priorityQ = []
answer = []

for _ in range(M):
    first, second = map(int, input().split())
    dic[first].append(second)
    indegree[second] += 1

for i in range(1,N+1):
    if indegree[i] == 0:
        heapq.heappush(priorityQ, i)
        # priorityQ.append(i)

while priorityQ:
    cur = heapq.heappop(priorityQ)
    # cur = priorityQ.popleft()
    answer.append(cur)
    for next in dic[cur]:
        indegree[next] -= 1
        if indegree[next]== 0:
            heapq.heappush(priorityQ, next)
            # priorityQ.append(next)

print(*answer)
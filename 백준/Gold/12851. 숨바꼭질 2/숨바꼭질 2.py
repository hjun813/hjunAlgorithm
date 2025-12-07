import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
q = []
heapq.heappush(q, (0, N))  # (초, 위치)
visit = [0 for _ in range(100001)]
visitMinSec = [float('inf') for _ in range(100001)]

minSec = float('inf')
way = 0
visit[N] = 1

while q:

    sec, s_now = heapq.heappop(q)

    if sec > minSec:
        break

    if s_now == K:
        minSec = min(minSec, sec)
        if minSec == sec:
            way += 1

    if 0 <= s_now-1 <= 100000:
        visit[s_now-1] += 1
        visitMinSec[s_now-1] = min(visitMinSec[s_now-1], sec+1)
        if visitMinSec[s_now-1] == sec+1:
            heapq.heappush(q, (sec + 1, s_now - 1))

    if 0 <= s_now+1 <= 100000:
        visit[s_now+1] += 1
        visitMinSec[s_now+1] = min(visitMinSec[s_now+1], sec+1)
        if visitMinSec[s_now+1] == sec+1:
            heapq.heappush(q, (sec + 1, s_now + 1))

    if 0 <= 2*s_now <= 100000: 
        visit[2*s_now] += 1   
        visitMinSec[s_now*2] = min(visitMinSec[s_now*2], sec+1)
        if visitMinSec[s_now*2] == sec+1:
            heapq.heappush(q, (sec + 1, 2 * s_now))

print(minSec)
print(way)
import sys

# from collections import deque
import heapq

N = int(sys.stdin.readline())
maxHq = []
minHq = []


mid = int(sys.stdin.readline())
heapq.heappush(maxHq, (-mid))
print(mid)

for i in range(1, N):
    k = int(sys.stdin.readline())

    if (-maxHq[0]) > k:
        heapq.heappush(maxHq, -k)
    elif (-maxHq[0]) <= k:
        heapq.heappush(minHq, k)
        if len(minHq)> len(maxHq):
            v = heapq.heappop(minHq)
            heapq.heappush(maxHq, -v)


    if len(maxHq) - len(minHq) >= 2:
        v = heapq.heappop(maxHq)
        heapq.heappush(minHq, -v)

    elif len(minHq) - len(maxHq) >= 2:
        v = heapq.heappop(minHq)
        heapq.heappush(maxHq, -v)

    # print("maxHq",maxHq, "minHq",minHq)
    print( (- maxHq[0]))

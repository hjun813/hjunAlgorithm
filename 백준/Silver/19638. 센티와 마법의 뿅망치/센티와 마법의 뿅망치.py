import heapq

import sys
input = sys.stdin.readline

N, H, T = map(int, input().split())
giants = []

for i in range(N):
    height = int(input())
    heapq.heappush(giants, -height)
    
cnt = 0

for i in range(T):
    
    check = heapq.heappop(giants)
    check = -check
    
    if check < H:
        heapq.heappush(giants, -check)
        break
    
    if check == 1:
        heapq.heappush(giants, -check)
        continue
    
    check = check / 2
    cnt += 1
    heapq.heappush(giants, -check)
    


check = heapq.heappop(giants)
check = -check

if  check >= H:
    print("NO")
    print(int(check))
else:
    print("YES")
    print(cnt)
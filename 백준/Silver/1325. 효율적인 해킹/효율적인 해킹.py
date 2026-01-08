import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
computer = {i: [] for i in range(1, N+1)}

for i in range(M):
    A, B = map(int, input().split())
    computer[B].append(A)

canAttack = [0 for _ in range(N)]

for i in range(1, N+1):
    
    check = deque([i])
    visit = [0 for _ in range(N)]
    visit[i-1] = 1
    while check:
        t = check.popleft()
        for j in computer[t]:
            if visit[j-1] == 0:
                visit[j-1] = 1
                check.append(j)
    canAttack[i-1] += sum(visit)
    
maxV = max(canAttack)
for i in range(N):
    if canAttack[i] == maxV:
        print(i+1, end=" ")

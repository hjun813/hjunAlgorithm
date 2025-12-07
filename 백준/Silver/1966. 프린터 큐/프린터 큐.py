import sys
from collections import deque

testN = int(sys.stdin.readline())

for _ in range(testN):

    N, M = map(int, sys.stdin.readline().split())

    importantN = list(map(int, sys.stdin.readline().split()))
    
    dq = deque()

    for i in range(N):
        dq.append([i, importantN[i]])

    count = 1

    while dq:
        
        for j in range(1, len(dq)):
            for k in range(len(dq)):
                if dq[0][1] >= dq[k][1]:
                    continue
                elif dq[0][1] < dq[k][1]:
                    r = dq.popleft()
                    dq.append(r)
                    break

        out = dq.popleft()
        # print('!!!', out)
        if out[0] == M:
            print(count)
            break

        count += 1          
    # print()  
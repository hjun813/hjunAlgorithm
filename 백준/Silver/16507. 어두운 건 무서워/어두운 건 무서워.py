import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())
brightL = []

for i in range(R):
    temp = list(map(int, input().split()))
    brightL.append(temp)

stackSum = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    temp = 0
    for j in range(C):
        temp += brightL[i][j]
        stackSum[i][j] = temp

# print(stackSum)

for i in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    cnt = (r2-r1+1)*(c2-c1+1)
    add = 0
    for k in range(r1, r2+1):
        # print(add)
        if c1 == 1:
            add += stackSum[k-1][c2-1]
        else:
            # print(stackSum[k-1][c2-1] , stackSum[k-1][c1-2])
            add += (stackSum[k-1][c2-1] - stackSum[k-1][c1-2])
    print(add // cnt)
    # print()
        
from collections import deque 

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dir = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
answer = 0
chess = deque([[r1, c1, 0]])
visit = [[0 for _ in range(N)] for _ in range(N)]
visit[r1][c1] = 1

while chess:
    nr, nc, cnt = chess.popleft()

    if nr == r2 and nc == c2:
        answer = cnt
        break
    
    for i in range(6):
        nnr = nr + dir[i][0]
        nnc = nc + dir[i][1]
        if 0<=nnr<N and 0<=nnc<N:
            if visit[nnr][nnc] == 0:
                visit[nnr][nnc] = 1
                chess.append([nnr, nnc, cnt+1])

if answer == 0:
    print(-1)
else:
    print(answer)
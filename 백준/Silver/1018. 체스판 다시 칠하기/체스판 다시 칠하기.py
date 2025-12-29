M, N = map(int, input().split())
chessBoard = [[0 for _ in range(N)] for _ in range(M)]
for i in range(M):
    temp = list(input().strip())
    for j in range(N):
        if temp[j] == 'B':
            chessBoard[i][j] = 1

result = 64

for i in range(M-7):
    for j in range(N-7):
        # i, j 가 시작점
        # white
        check_w = 0
        for a in range(8):
            for b in range(8):
                if (a+b) % 2 == 0:
                    if chessBoard[i+a][j+b] != 0:
                        check_w += 1
                else:
                    if chessBoard[i+a][j+b] != 1:
                        check_w += 1
        check_b = 0
        for a in range(8):
            for b in range(8):
                if (a+b) % 2 == 0:
                    if chessBoard[i+a][j+b] != 1:
                        check_b += 1
                else:
                    if chessBoard[i+a][j+b] != 0:
                        check_b += 1
        result = min(check_w, check_b, result)

print(result)
import sys, math
input = sys.stdin.readline

T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    move = y - x
    answer = 0
    n = int(math.sqrt(move))
    check = (1 + n) * n 
    if move == n*n:
        answer = n * 2 - 1
    elif n*n < move <= check:
        answer = n * 2
    else:
        answer = n * 2 + 1
    print(answer)

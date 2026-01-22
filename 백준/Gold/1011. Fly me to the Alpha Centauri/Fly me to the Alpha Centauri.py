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

# 풀이 과정
# 일단 처음과 끝은 항상 1이다
# 그래서 일단 계산을 해봄
# 범위가 0 < x <= y < 2^31이라 2의 거듭제곱을 의심하긴 했는데 얘는 의미 없었음
# 범위를 나눠서 보니까 이런 구간에서 갈림
# 1, 11, 121(4), 1221, 12321(9), 123321, 1234321(16) ....
# 그래서 제곱수로 대략적인 위치를 파악하고
# 12..n..21 과 12..nn..21 그리고 그 이상 인지를 따져서 횟수 계산

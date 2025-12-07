import sys
input = sys.stdin.readline

N = int(input())
work = []
score = 0

for _ in range(N):
    get = input().strip()
    if get == '0':

        if work:
            getScore, time = work.pop()
            if (time-1) > 0:
                work.append((getScore,time-1))
            else:
                score += getScore

    else:
        one, A, T = map(int, get.split())
        
        if (T-1) > 0:
            work.append((A, T-1))
        else:
            score += A

print(score)
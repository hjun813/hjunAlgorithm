L, N, T = map(int, input().split())
ball = []
for i in range(N):
    p, d = input().split()
    p = int(p)
    ball.append([p, d])

cnt = 0
for t in range(T+1):
    
    ball.sort()
    # 충돌 찾아야 함 -> 방향만 변경
    # 1. 벽 충돌 
    # 2. 공 충돌
    bf_p = 0
    for n in range(N):
        if ball[n][0] == 0:
            ball[n][1] = 'R'
        elif ball[n][0] == L:
            ball[n][1] = 'L'
        elif ball[n][0] == bf_p:
            ball[n-1][1] = 'L'
            ball[n][1] = 'R'
            cnt += 1
            
        bf_p = ball[n][0]


    for n in range(N):
        if ball[n][1] == 'R':
            ball[n][0] += 1
        else:
            ball[n][0] -= 1

print(cnt)
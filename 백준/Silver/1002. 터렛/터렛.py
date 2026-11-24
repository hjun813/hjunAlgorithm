# 거리공식으로 처리해야하네
# 근데 보통은 2개
# 일치는 1개
# 무수히 많은건 다같을때
# 없는건 짧을때

T = int(input())
for t in range(T):
    answer = 0

    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if x1 == x2 and y1 == y2 and r1 == r2: # 동일한 원일때
        answer = -1

    elif r > r1 and r > r2:
        # 중심이 하나의 원 안에 없을때
        # 길이만 3가지 경우 비교해주면 됨
        if r1 + r2 < r:
            answer = 0
        elif r1 + r2 == r:
            answer = 1
        else:
            answer = 2
    
    else:
        # 중심이 하나의 원안에 있음
        # 두점사이거리 + 하나의 거리가 나머지 길이보다 크면 2개, 같으면 1개 작으면 0개 
        if r + min(r1, r2) > max(r1, r2):
            answer = 2
        elif r + min(r1, r2) == max(r1, r2):
            answer = 1
        else:
            answer = 0
    print(answer)
    
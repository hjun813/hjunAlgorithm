t, x, m = map(int, input().split())
monster = []
canTime = float('inf')
flag = 0
answer = 0
for i in range(m):
    d, s = map(int, input().split())
    if d == 0:
        flag = 1
        break
    monster.append([d, s])
    ct = (d-1) // s
    canTime = min(canTime, ct)
    # t시간 만큼 시간당 x개를 주울수 있는데
    # 줍는 중에는 s 만큼 다가오고
    # 아니면 돌아감

    # 시간 돌면서 1,000,000
    # 몬스터 만큼 1,000 = 1,000,000,000
    # 0 보다 작거나 같게 되면 돌아가게

    # 시간 초과 날꺼 같은디

    # 아님 입력 받을 때 몇턴까지 버틸수 있는지 보는거임
    # 글고 와리가리 치면 되는거 아님?
    # 남은 턴에서 2나눠서
if flag == 0:
    if canTime == 0:
        answer = 0
    else:
        if t <= canTime:
            answer = x * t
        else:
            answer = x * canTime + x * ((t - canTime)//2) 
else:
    answer = 0
print(answer)
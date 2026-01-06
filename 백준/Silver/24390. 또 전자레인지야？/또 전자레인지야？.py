# 10초, 60초, 600초, 조리시작
# 조리시작 {1.조리중 : 30초 추가 2. 조리중 X : 시작, 0초시 30초 추가후 시작}

M, S = map(int, input().split(":"))
minute = M * 60 + S

activate = 0
time = 0

cnt = 0

cnt += minute // 600
minute = minute % 600
cnt += minute // 60
minute = minute % 60
# 이러면 이제 0초부터 50초가 남음
if minute == 0:
    cnt += 1
    activate = 1
else:
    if minute >= 30:
        
        cnt += 1
        activate = 1
        minute -= 30
    cnt += minute // 10
    if activate == 0:
        cnt += 1
print(cnt)
        

# 그리디로 푼다면
# 무조건 600초가 이득, 그다음은 60초, 그다음은 10초 이건데
# 생각해야하는건 조리시작은 30초 + activate임
# 그럼 activate 일때는 30초 버튼이 있는거고
# activate가 아닐때는 0초 일때
    
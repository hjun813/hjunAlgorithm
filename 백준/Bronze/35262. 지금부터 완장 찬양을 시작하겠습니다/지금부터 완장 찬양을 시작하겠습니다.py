N, K = map(int, input().split())
attendance = list(input())
answer = 1
combo = 0
for i in range(N):
    if combo >= K:
        answer = 0
        break
    
    if attendance[i] == '1':
        combo = 0
    else:
        combo += 1

if combo >= K:
    answer = 0
print(answer)
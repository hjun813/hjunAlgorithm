N, K = map(int, input().split())
people = []
answer = set([])
for i in range(N):
    get = list(map(int, input().split()))
    people.append(get)

for k in range(K):
    for i in range(N): # 비교
        f2 = 0
        for j in range(N): # 비교 대상
            if i != j:
                if people[i][k] <= people[j][k]: # 안됨
                    f2 = 1
                    break
        if f2 == 0: # 찾음
            answer.add(i)
            break
if N == 1:
    print(1)
else:
    print(len(answer))
        
            

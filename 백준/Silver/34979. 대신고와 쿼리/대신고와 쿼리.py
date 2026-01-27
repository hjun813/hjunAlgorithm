N, Q = map(int, input().split())
classStress = [[0 for _ in range(N)] for _ in range(4)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]
maxStressClass = 0
maxStressClassIdx_x = 1
maxStressClassIdx_y = 1

for i in range(Q):
    query = list((input().split()))
    
    if query[0] == "2":
        # 제일 높은 데 출력
        query[0] = int(query[0])
        query[1] = int(query[1])
        a = query[1] - 1
        maxStress = 0
        idx = 1
        for j in range(N):
            maxStress = max(maxStress, classStress[a][j])
        for j in range(N-1, -1, -1):
            if maxStress == classStress[a][j]:
                idx = j
        print(idx+1)

    else:
        query[0] = int(query[0])
        query[1] = int(query[1])
        query[2] = int(query[2])
        a = query[1] - 1
        b = query[2] - 1 
        classStress[a][b] += 1
        for j in range(4):
            if 0 <= a+dir[j][0] < 4 and 0 <= b+dir[j][1] < N:
                classStress[a+dir[j][0]][b+dir[j][1]] += 1
    
        
for i in range(3,-1,-1):
    for j in range(N-1, -1, -1):
        maxStressClass = max(maxStressClass, classStress[i][j])
for i in range(3,-1,-1):
    for j in range(N-1, -1, -1):
        if maxStressClass == classStress[i][j]:
            maxStressClassIdx_x = i
            maxStressClassIdx_y = j
print(maxStressClassIdx_x+1, maxStressClassIdx_y+1)
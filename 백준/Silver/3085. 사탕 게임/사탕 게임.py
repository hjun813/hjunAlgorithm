N = int(input())
mapInfo = [[0 for _ in range(N)] for _ in range(N)]
dir = [[0, 1], [1, 0]]
answer = 0

def maxVal(board):
    max_cnt = 1
    for i in range(len(board)):
        # 가로 확인
        cnt = 1
        for j in range(1, len(board)):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
        
        # 세로 확인
        cnt = 1
        for j in range(1, len(board)):
            if board[j][i] == board[j-1][i]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
    return max_cnt
    
for i in range(N):
    get = list(input())
    for j in range(len(get)):
        if get[j] == 'P':
            mapInfo[i][j] = 1
        elif get[j] == 'Z':
            mapInfo[i][j] = 2
        elif get[j] == 'Y':
            mapInfo[i][j] = 3

for i in range(N):
    for j in range(N):
        for k in range(2):
            if 0 <= dir[k][0] + i < N and 0 <= dir[k][1] + j < N:
                if mapInfo[i][j] != mapInfo[dir[k][0] + i][dir[k][1] + j]:
                    temp = mapInfo[i][j]
                    mapInfo[i][j] = mapInfo[dir[k][0] + i][dir[k][1] + j]
                    mapInfo[dir[k][0] + i][dir[k][1] + j] = temp
                    t = maxVal(mapInfo)
                    answer = max(answer, t)
                    temp = mapInfo[i][j]
                    mapInfo[i][j] = mapInfo[dir[k][0] + i][dir[k][1] + j]
                    mapInfo[dir[k][0] + i][dir[k][1] + j] = temp

print(answer)
                    
                    

    

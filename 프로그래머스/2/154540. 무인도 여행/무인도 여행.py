from collections import deque

def solution(maps):
    answer = []
    maplen = len(maps)
    mapInfo = [] 
    for i in range(maplen):
        l = list(maps[i])
        mapInfo.append(l)
    
    dirX = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0 for _ in range(len(mapInfo[0]))] for _ in range(maplen)]
    
    for i in range(maplen):
        for j in range(len(mapInfo[0])):
            if visited[i][j] == 0 and mapInfo[i][j] != 'X':
                # 여기서 dfs나 bfs로 찾기
                q = deque([])
                tmp = 0
                q.append([i,j])
                visited[i][j] = 1
                
                while q:
                    x, y = q.popleft()
                    tmp += int(mapInfo[x][y])
                    
                    for d in range(4):
                        nx = x + dirX[d][0]
                        ny = y + dirX[d][1]
                        if 0 <= nx < maplen and 0 <= ny < len(mapInfo[0]):
                            if visited[nx][ny] == 0:
                                if mapInfo[nx][ny] != 'X':
                                    visited[nx][ny] = 1
                                    q.append([nx,ny])
                answer.append(tmp)  
                
    if len(answer) > 0:
        answer.sort()
        return answer
    else:
        return [-1]
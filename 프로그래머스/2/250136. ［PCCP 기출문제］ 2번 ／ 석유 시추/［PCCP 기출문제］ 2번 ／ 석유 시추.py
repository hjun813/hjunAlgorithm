from collections import deque

def solution(land):
    answer = 0
    
    n = len(land)
    m = len(land[0])
    
    dire = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    oil = [[0 for _ in range(m)] for _ in range(n)]
    
    num = 2
    findQ = deque([])
    res = {}
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                tmp = 0
                land[i][j] = num
                findQ.append([i, j])
                while findQ:
                    ti, tj = findQ.popleft()
                    tmp += 1
                    for k in range(4):
                        ni = ti + dire[k][0]
                        nj = tj + dire[k][1]
                        if 0 <= ni and ni < n and 0 <= nj and nj < m:
                            if land[ni][nj] == 1:
                                land[ni][nj] = num
                                findQ.append([ni, nj])
                
                res[num] = tmp
                num += 1
    
    for i in range(m):
        can = set([])
        t = 0
        for j in range(n):
            if land[j][i] != 0:
                can.add(land[j][i])
        for c in can:
            t += res[c]
        answer = max(answer, t)
        
    return answer
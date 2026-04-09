def solution(triangle):
    answer = 0
    temp = []
    for i in range(len(triangle)):
        tmp = []
        if i == 0:
            tmp.append(triangle[0][0])
            
        else:
            for k in range(i+1):
                if k == 0:
                    tmp.append(temp[i-1][0] + triangle[i][k])
                elif k == i:
                    tmp.append(temp[i-1][-1] + triangle[i][k])
                else:
                    tmp.append(triangle[i][k] + max(temp[i-1][k-1] , temp[i-1][k]))
        temp.append(tmp)
    answer = max(temp[-1])

    return answer


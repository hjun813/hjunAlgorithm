N = int(input())
have = []
answer = ""

def check(mapInfo, a, b, n):
    global answer
    temp = mapInfo[a][b]
    flag = 0
    for i in range(n):
        for j in range(n):
            if mapInfo[a+i][b+j] != temp:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        answer = answer + '('
        check(mapInfo, a, b, n//2)
        check(mapInfo, a, b+n//2, n//2)
        check(mapInfo, a+n//2, b, n//2)
        check(mapInfo, a+n//2, b+n//2, n//2)
        answer = answer + ')'
    else:
        answer += temp
        
    
for i in range(N):
    get = list(input())
    have.append(get)

check(have, 0,0, N)
print(answer)
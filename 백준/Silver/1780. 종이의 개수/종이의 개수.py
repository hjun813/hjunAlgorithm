N = int(input())
paper = []
answer1 = 0
answer2 = 0
answer3 = 0

for i in range(N):
    temp = list(map(int, input().split()))
    paper.append(temp)

def papercheck(x, y, n):

    global answer1
    global answer2
    global answer3
    
    number = paper[x][y]
    flag = 0
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != number:
                flag = 1
                break
    if flag == 1:
        # 새로운 재귀 돌기
        nn = n//3
        papercheck(x,y,nn)
        papercheck(x+nn,y,nn)
        papercheck(x+2*nn,y,nn)
        
        papercheck(x,y+nn,nn)
        papercheck(x+nn,y+nn,nn)
        papercheck(x+2*nn,y+nn,nn)
        
        papercheck(x,y+2*nn,nn)
        papercheck(x+nn,y+2*nn,nn)
        papercheck(x+2*nn,y+2*nn,nn)
        
    else:
        if number == -1:
            answer1 += 1
        elif number == 0:
            answer2 += 1
        else:
            answer3 += 1
        
        
papercheck(0,0,N)    
print(answer1)
print(answer2)
print(answer3)
    
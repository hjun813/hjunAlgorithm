import sys
input=sys.stdin.readline
N,K=map(int,input().split())
lst=[]
answer = set([])
cnt=0
l=0 
s=[[] for _ in range(K)]
for i in range(N):
    lst.append(list(map(int,input().split())))
    for j in range(K):
        s[j].append(lst[i][j])

if N==1:
    print(N)
else:
    for x in range(K):
        c=0
        l=max(s[x])
        temp = 0
        for y in range(N):
            if s[x][y]==l:
                c+=1
                temp=y
                
        if c == 1:
            answer.add(temp)
    
    print(len(answer))

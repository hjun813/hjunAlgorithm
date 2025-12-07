import math

G = int(input())

check = int(math.sqrt(G))
answer =[]

for i in range(1, check+1):
    
    if G % i == 0:
        remain = G / i
        if (remain + i) % 2 == 0:
            a = int((remain + i) // 2)
            if a*a != G:
                answer.append(a)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
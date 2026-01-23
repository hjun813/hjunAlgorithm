from collections import deque

N = int(input())
waiting = deque(list(map(int, input().split())))
answer = "Nice"

temp = []

for i in range(1, N+1):

    while True:
        if len(waiting) != 0:
            if waiting[0] != i:
                
                if len(temp) != 0 and temp[-1] == i:
                    temp.pop()
                    break
                else:
                    t = waiting.popleft()
                    temp.append(t)
            else:
                waiting.popleft()
                break
        else:
            if temp[-1] == i:
                temp.pop()
                break
            else:
                answer = "Sad"
                break

    if answer == "Sad":
        break

print(answer)
        
    


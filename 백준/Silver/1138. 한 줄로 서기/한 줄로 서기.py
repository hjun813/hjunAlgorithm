import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
left = list(map(int, input().split()))
height = []
answer = deque(height)

# for i in range(N-1, -1, -1):
#     temp = []
#     for j in range(N+1 - i):
#         if j == left[i]:
#             temp.append(i)
#         else:
#             temp.append(answer[i])

for i in range(N):
    index = N - 1 - i
    temp = []
    if index == N:
        answer.append(N)
        continue
        
    leftNum = left[index]
    
    for j in range(i+1):
        if j == leftNum:
            temp.append(index+1)
            continue
        temp.append(answer.popleft())
        
    for j in temp:
        answer.append(j)
        
print(*answer)
        

# for i in range(N):
    
#     index = N - 1 - i
#     temp = []
#     cnt = 0
#     print("------------!")
#     print(*answer)
#     print("------------!!")
    
#     if i == 0:
#         answer.append(N)
#         continue
    
#     for j in answer:
#         if cnt == left[index]:
#             temp.append(index+1)                    
#         temp.append(j)
#         answer.popleft()
#         cnt += 1
        
#     print(*temp) 
    
#     for j in temp:
#         answer.append(j) 
        
#     print(*answer)
#     print('-------------------')
        
# print(*answer)

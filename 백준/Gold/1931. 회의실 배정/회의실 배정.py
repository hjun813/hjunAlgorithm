import sys
input = sys.stdin.readline

N = int(input())
Plan = []

for i in range(N):
    start, end = map(int, input().split())
    Plan.append((end, start))
    
Plan.sort()
cnt = 0
b_start = 0
b_end = 0

for i in range(N):
    
    if i == 0:
       cnt += 1
       b_start = Plan[i][1]
       b_end = Plan[i][0]
       continue
       
    if Plan[i][1] >= b_end:
        cnt += 1
        b_start = Plan[i][1]
        b_end = Plan[i][0]
        
print(cnt)
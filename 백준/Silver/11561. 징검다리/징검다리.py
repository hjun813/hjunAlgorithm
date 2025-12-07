import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    
    left = 1
    right = N
    
    if N == 1:
        mid = 1
        
    while(left < right):
        
        if left == right -1:
            mid = left
            break
        
        mid = (left + right) // 2

        
        
        if((1 + mid) * mid * 0.5 == N):
            break
        elif((1 + mid) * mid * 0.5> N):
            right = mid 
        else:
            left = mid 
 
    
    print(mid)
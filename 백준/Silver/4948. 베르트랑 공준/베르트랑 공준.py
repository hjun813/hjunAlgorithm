import sys
from collections import deque
input = sys.stdin.readline

while(True):
    n = int(input())
    if (n == 0):
        break
    if (n == 1):
        print(1)
        continue
    if (n == 2):
        print(1)
        continue

    maxDivide = int((2*n)**0.5) +1
    
    check = deque([])

    for num in range(n+1, (2*n)+1):
        for divide in range(2, maxDivide+1):
            if num % divide == 0:
                break
            if divide == maxDivide and num % divide != 0:
                check.append(num)
    
    print(len(check))

        


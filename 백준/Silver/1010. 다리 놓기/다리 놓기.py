T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    # MCN 구하기
    a = 1
    for i in range(N):
        a = a * (M-i)
    for i in range(N):
        a = a // (i+1)
    
    print(a)  
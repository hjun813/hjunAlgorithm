T = int(input())
for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    new = [0 for _ in range(N)]
    a = 0
    b = 0
    for j in range(N):
        if j % 2 == 0:
            new[a] = L[j]
            a += 1
        else:
            t = -1-b 
            new[t] = L[j]
            b += 1
    
    level = 0
    for j in range(N):
        if j == N-1:
            level = max(level, abs(new[j] - new[0]))
        else:
            level = max(level, abs(new[j] - new[j+1]))
    print(level)
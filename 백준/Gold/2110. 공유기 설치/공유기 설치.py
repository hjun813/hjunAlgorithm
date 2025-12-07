import sys
N, C = map(int, sys.stdin.readline().split())
home = []

for _ in range(N):
    home.append(int(sys.stdin.readline()))
home.sort()

# 간격을 이분탐색하여 최적의 거리 찾기!
low = 1
high = home[-1]

answer = 0

while low <= high:

    mid = (low + high) // 2
    installed = 1
    last_installed = home[0]

    for i in range(1,N):
        if home[i] - last_installed >= mid:
            installed += 1 
            last_installed = home[i]

    if installed >= C: 
        answer = mid
        low = mid +1 

    elif installed < C:
        high = mid -1 

print(answer)
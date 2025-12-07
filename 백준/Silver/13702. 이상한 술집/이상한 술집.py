N, K = map(int, input().split())
mak = []
for i in range(N):
    mak.append(int(input()))

left = 0
right = max(mak) * 2
bfmid = 0

while True:

    mid = (left + right) // 2
    
    if bfmid == mid:
        break
    # 탈출 조건
    if left > right:
        break
    
    temp = 0
    for i in range(N):
        a = mak[i] // mid
        temp += a
    
    if temp > K: # 너무 조금
        left = mid + 1
    elif temp == K: # 더 담을 수 있는지 체크 해야함
        left = mid + 1
    elif temp < K:
        right = mid - 1

    bfmid = mid

print(mid)
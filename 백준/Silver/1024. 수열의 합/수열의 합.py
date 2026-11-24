N, L = map(int, input().split())

# 연속된 수의 합이 N 이어야 하고
# 개수는 L 이상

# 시작이 K이고 개수가 L라 하면
# L * K + (L * (L - 1) / 2)
# L * ( 2K + L - 1 ) / 2 = N
# 2K + L - 1 = 2 * N / L
# 2K = ((2 * N / L) + 1 - L)
# L을 올려서 K값을 구하는데
# K가 정수여야함
l = L
k = 0
flag = 0

while True:
    get = (N * 2 / l) + 1 - l
    if get < 0:
        flag = 1
        break
    if get % 2 == 0:
        k = get / 2
        break
    else:
        l += 1

if flag == 0 and l <= 100:
    for i in range(l):
        print(int(k+i), end=" ")
else:
    print(-1)
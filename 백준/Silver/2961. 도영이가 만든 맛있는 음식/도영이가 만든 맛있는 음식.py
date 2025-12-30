from itertools import combinations

N = int(input())
flavor = []
for i in range(N):
    S, B = map(int, input().split())
    flavor.append([S, B])
    
# S 는 곱, B 는 합
# 다 계산 해야 하나?
# N 이 10 이하니까 경우의 수는 음...


def check(s, b, n, m, arr):
    if n == N:
        if not m == 0:
            arr.append(abs(s - b))
    if n < N:
        check(flavor[n][0] * s , flavor[n][1] + b, n+1, m+1, arr)
        check(s, b, n+1, m, arr)
    
arr = []
check(1, 0, 0, 0, arr)
print(min(arr))
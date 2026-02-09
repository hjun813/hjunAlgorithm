N, m =  map(int, input().split())
ans = 1
t1 = N
t2 = N // 2
t3 = N // 2 + N % 2
t4 = (N-1) // 3 + 1

if N == 1:
    if m >= 1:
        ans = 2
elif N == 2:
    if m == 1:
        ans = 3
    if m >= 2:
        ans = 4
else:
    if m >= t1:
        ans += 1
    if m >= t2:
        ans += 1
    if m >= t3:
        ans += 1
    if m >= t4:
        ans += 1
    if m >= t2 + t4:
        ans += 1
    if m >= t3 + t4:
        ans += 1
    if m >= t1 + t4:
        ans += 1
print(ans)
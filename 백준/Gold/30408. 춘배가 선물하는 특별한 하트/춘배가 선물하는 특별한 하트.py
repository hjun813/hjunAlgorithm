N, M = map(int, input().split())
answer = "NO"
left = M
right = M
if N == M:
    answer = "YES"
    print(answer)
else:
    while True:
        if left == 1:
            left = 2
        else:
            left = left * 2 - 1
        right = right * 2 + 1
        if left <= N <= right:
            answer = "YES"
            break
        if N < left:
            break
    print(answer)
L = int(input())
S = list(map(int, input().split()))

n = int(input())
# n을 포함하는 구간중 
# 모든 수가 집합에 없는거
answer = 0
S.sort()
if n in S:
    answer = 0
else:
    if L == 1:
        answer = 0
    else:
        check = 0
        for i in range(L):
            if S[i] >= n:
                check = i - 1
                break

        if check == -1:
            l = 1
            r = S[check+1] - 1
            left = n - l
            right = r - n
            answer = left * (right + 1) + right

        else:
            l = S[check] + 1
            r = S[check+1] - 1
            left = n - l
            right = r - n
            answer = left * (right + 1) + right

print(answer)
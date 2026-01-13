from collections import deque
N, S, M = map(int, input().split())
V = list(map(int, input().split()))
# 현재 볼륨 P 이면, i 번째 곡은 P+V[i] 나 P-V[i], 0보다 작거나 M보단 크면 안됨
# 마지막 곡 최댓값
# 볼륨을 빼거나 더할 수 있거든?
# 일단 dp[i]를 i 번째 최대 볼륨이라 하자
# 그럼 i + 1은 어떻게 될까?
# dp[i+1] = dp[i] + v[i]인데 M을 넘으면 안되고
# dp[i+1] = dp[i] - v[i]는 아닐수도 있고

# 배열에 넣고 하나씩 빼면서 두가지 경우 넣어주기
# 메모리 초과
answer = 0
check = set()
check.add(S)
for i in range(N+1):
    l = len(check)
    if l == 0:
        answer = -1
        break

    if i == N:
        answer = max(check)
        break;
    newS= set()  
    for j in range(l):
        tmp = check.pop()
        if 0 <= tmp + V[i] <= M:
            newS.add(tmp + V[i])
        if 0 <= tmp - V[i] <= M:
            newS.add(tmp - V[i])
    check = newS
print(answer)

# dp[i][] =>0은 더햇을때 최대, 1은 뺏을때 최대
# 틀림
# dp = [[0 for _ in range(2)] for _ in range(N)]

# for i in range(N):
    
#     if i == 0:
#         if 0<= S + V[i] <= M:
#             dp[i][0] = S + V[i]
#         else:
#             dp[i][0] = -1
#         if 0<= S - V[i] <= M:
#             dp[i][1] = S - V[i]
#         else:
#             dp[i][1] = -1

#     else:
#         if dp[i-1][0] != -1:
#             if 0 <= dp[i-1][0] + V[i] <= M:
#                 dp[i][0] = dp[i-1][0] + V[i]
#         if dp[i-1][1] != -1:
#             if 0 <= dp[i-1][1] + V[i] <= M:
#                 dp[i][0] = max(dp[i][0], dp[i-1][1] + V[i])
#         if dp[i][0] == 0:
#             dp[i][0] = -1

#         if dp[i-1][0] != -1:
#             if 0 <= dp[i-1][0] - V[i] <= M:
#                 dp[i][1] = dp[i-1][0] - V[i]
#         if dp[i-1][1] != -1:
#             if 0 <= dp[i-1][1] - V[i] <= M:
#                 dp[i][1] = max(dp[i][1], dp[i-1][1] - V[i])
#         if dp[i][1] == 0:
#             dp[i][1] = -1

# print(dp)
# print(max(dp[-1][0], dp[-1][1]))

# 재귀로 풀기
# 시간 초과
# answer = -1
# def play(p, n):
#     global answer
    
#     if n == N:
#         answer = max(answer, p)
#         return
#     # 더한거
#     if 0 <= p + V[n] <= M:
#         play(p + V[n], n+1)
        
#     if 0 <= p - V[n] <= M:
#         play(p - V[n], n+1)

# play(S, 0)
# if answer == -1:
#     print(-1)
# else:
#     print(answer)

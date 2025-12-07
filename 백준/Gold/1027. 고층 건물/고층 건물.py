import sys
input = sys.stdin.readline

N = int(input())
building = list(map(int, input().split()))
answer = [0 for _ in range(N)]

for i in range(N):
    max_slope = -float('inf')
    for j in range(i+1, N):
        slope = (building[j] - building[i]) / (j - i)
        if slope > max_slope:
            max_slope = slope
            answer[i] += 1
            answer[j] += 1

print(max(answer))

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

direction = [(1,0), (-1,0), (0,1), (0,-1)]
dp = [[-1]*N for _ in range(M)]  # -1이면 아직 방문하지 않음

def dfs(x, y):
    if x == M-1 and y == N-1:
        return 1  # 목적지 도달

    if dp[x][y] != -1:
        return dp[x][y]  # 이미 계산된 경로 수 반환

    dp[x][y] = 0
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))

import sys
from collections import deque

# 입력 받기
N = int(sys.stdin.readline())  # 맵 크기
K = int(sys.stdin.readline())  # 사과 개수

# 사과 위치 저장 (set 사용 -> O(1) 탐색)
apples = set()
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    apples.add((x, y))

L = int(sys.stdin.readline())  # 방향 변환 횟수
rotations = {}  # {시간: 방향} 딕셔너리
for _ in range(L):
    sec, rot = sys.stdin.readline().split()
    rotations[int(sec)] = rot

# 방향 (우, 하, 좌, 상) -> 시계방향 기준
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 초기 설정
snake = deque([(1, 1)])  # 뱀 위치 (머리가 첫 번째 원소)
direction_idx = 0  # 초기 방향 (오른쪽)
time = 0  # 시간

# 게임 실행
while True:
    time += 1
    
    # 현재 방향으로 머리 이동
    head_x, head_y = snake[0]
    dx, dy = DIRECTIONS[direction_idx]
    new_head = (head_x + dx, head_y + dy)
    
    # 벽 충돌 체크
    if not (1 <= new_head[0] <= N and 1 <= new_head[1] <= N):
        break
    
    # 자기 몸과 충돌 체크
    if new_head in snake:
        break
    
    # 이동
    snake.appendleft(new_head)
    
    # 사과 여부 확인
    if new_head in apples:
        apples.remove(new_head)  # 사과 먹음 (길이 유지)
    else:
        snake.pop()  # 사과 없으면 꼬리 제거 (길이 유지)
    
    # 방향 전환 체크
    if time in rotations:
        if rotations[time] == 'D':  # 오른쪽 회전 (시계 방향)
            direction_idx = (direction_idx + 1) % 4
        elif rotations[time] == 'L':  # 왼쪽 회전 (반시계 방향)
            direction_idx = (direction_idx - 1) % 4

# 게임 종료 후 걸린 시간 출력
print(time)

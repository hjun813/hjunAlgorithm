import heapq
import sys

input = sys.stdin.readline

N = int(input())
classes = []

for _ in range(N):
    s, e = map(int, input().split())
    classes.append((s, e))

# 1. 시작 시간 기준으로 오름차순 정렬
classes.sort()

# 2. 강의실의 '종료 시간'을 관리할 최소 힙
rooms = []
# 첫 번째 강의의 종료 시간을 넣고 시작
heapq.heappush(rooms, classes[0][1])

for i in range(1, N):
    start, end = classes[i]
    
    # 가장 빨리 비는 강의실(rooms[0])의 종료 시간과 현재 강의 시작 시간 비교
    if rooms[0] <= start:
        # 이 방을 그대로 쓸 수 있으므로 기존 종료 시간을 빼줌
        heapq.heappop(rooms)
    
    # 새로운 종료 시간(또는 갱신된 시간)을 힙에 추가
    heapq.heappush(rooms, end)

# 힙에 남아있는 원소의 개수가 필요한 최소 강의실 수입니다.
print(len(rooms))
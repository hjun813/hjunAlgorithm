import heapq
A, B = map(int, input().split())

# 2를 곱한다 혹은 1을 오른쪽에 붙인다.
# A가 B 될때까지
# 없는 경우는 -1
# 힙에 넣고 최소 보면서 넘어가면 안넣고 ㅇㅈ?

change = []
answer = -2

heapq.heappush(change, [0, A])

while change:
    n, number = heapq.heappop(change)
    if number == B:
        answer = n
        break
    if number * 2 <= B:
        heapq.heappush(change, [n+1, number*2])
    if number * 10 + 1 <= B:
        heapq.heappush(change, [n+1, number * 10 + 1])

print(answer+1)
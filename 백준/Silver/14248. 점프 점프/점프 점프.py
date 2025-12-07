import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

rock = list(map(int, input().split()))
temp = deque([])

now = int(input())
nowIndex = now -1

visited = [0 for _ in range(n)]
visited[nowIndex] = 1
can = 1
temp.append(now)


def bfs():

    while temp:
        global can
        a = temp.popleft()
        b = rock[a-1]
        
        if 0< a + b < n+1:
            if visited[a+b-1] == 0:
                can += 1
                visited[a+b-1] = 1
                temp.append(a+b)
                
        if 0< a - b < n+1:
            if visited[a-b-1] == 0:
                can += 1
                visited[a-b-1] = 1
                temp.append(a-b)

bfs()
print(can)
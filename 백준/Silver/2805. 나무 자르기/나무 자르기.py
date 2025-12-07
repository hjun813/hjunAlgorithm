
import sys

n, m = map(int, sys.stdin.readline().split())

height = list(map(int, sys.stdin.readline().split()))
height.sort()
maxHeight = height[n - 1]
getTree = []
get = 0


def binarySearch(n, start, end):
    global get

    if start > end:
        return None
    
    mid = (start + end) // 2

    for i in range(n):
        if height[i] > mid:
            get = get + height[i] - mid

    # print("get ", get, " m ", m, " start ", start," mid ", mid, " end ", end)

    if get < m:
        if start == end:
            return start-1
        get = 0
        return binarySearch(n, start, mid - 1)
    elif get > m:
        if start == end:
            return start
        get = 0
        return binarySearch(n, mid + 1, end)
    elif get == m:
        return mid

print(binarySearch(n , 0, maxHeight))
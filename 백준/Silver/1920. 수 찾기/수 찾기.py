
import sys

n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
nList.sort()

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))


def binarySearch(n, arr, start, end):

    if start < end:
        
        mid = int((start + end) // 2)

        if n == arr[mid]:
            return print(1)
        elif n < arr[mid]:
            binarySearch(n, arr, start, mid - 1)
        else:
            binarySearch(n, arr, mid + 1, end)

    elif start == end:
        mid = start
        if n == arr[mid]:
            return print(1)
        else :
            return print(0)
        
    else : 
        print(0)

for i in range(m):
    
    binarySearch(mList[i], nList, 0, n - 1)

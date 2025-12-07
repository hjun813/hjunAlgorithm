import sys
N = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))

cardList.sort()


for i in checkList:
   
    left = 0
    right = N -1

    while left <= right:
        mid = (left+ right) // 2
        
        if cardList[mid] == i:
            print(1)
            break

        elif cardList[mid] < i:
            left = mid + 1
        
        elif cardList[mid] > i:
            right = mid - 1
    
    if left > right and cardList[mid] != i:
        print(0)


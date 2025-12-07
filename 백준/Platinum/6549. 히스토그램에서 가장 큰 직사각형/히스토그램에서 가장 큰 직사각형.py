import sys


def function1(arr):

    maxSquare = 0
    check = [[-1, -1]]

    for i in range(len(arr)):
        if arr[i] > check[-1][1]:
            check.append([i, arr[i]])
        else:
            while check[-1][1] >= arr[i]:

                [idx, h] = check.pop()
                tmp = (i - idx) * h
                maxSquare = max(maxSquare, tmp)
            check.append([idx, arr[i]])

    # print(maxSquare)
    # print(check)

    while check:
        i, h = check.pop()
        w = n - i
        # print(h * w)
        maxSquare = max(maxSquare, h * w)


    return maxSquare


while True:
    recInfo = list(map(int, sys.stdin.readline().split()))
    if len(recInfo) == 1:
        break
    n = recInfo[0]
    recHeight = recInfo[1 : len(recInfo)]

    print(function1(recHeight))

N = int(input())
arr = list(map(int, input().split()))
orderedArr = [0] * N
used = [False] * N
between = [0] * (N-1)
betweenList = []

def orderArr(arr, n):
    if n < N:
        for i in range(N):
            if not used[i]:
                orderedArr[n] = arr[i]
                used[i] = True
                orderArr(arr, n + 1)
                used[i] = False
    elif n == N:
        # print(orderedArr)
        for i in range(len(orderedArr)-1):
            if orderedArr[i] - orderedArr[i+1] < 0:
                between[i] = -(orderedArr[i] - orderedArr[i+1])
            else:
                between[i] = orderedArr[i] - orderedArr[i+1]
        betweenList.append(sum(between))


orderArr(arr, 0)
print(max(betweenList))

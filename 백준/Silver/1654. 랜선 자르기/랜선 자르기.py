K, N = map(int, input().split())
lenString = []
for i in range(K):
    get = int(input())
    lenString.append(get)
lenString.sort()

left = 1
right = lenString[-1]

while left <= right:
    
    mid = (left + right) // 2
    have = 0
    for i in range(K):
        have += (lenString[i] // mid)
    if have >= N :
        left = mid + 1
    elif have < N:
        right = mid - 1

print(right)
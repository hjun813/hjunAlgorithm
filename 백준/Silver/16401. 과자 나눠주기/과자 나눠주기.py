M, N = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort()
answer = 0

# 딱 봐도 이분 탐색임

left = 1
right = snack[-1]

if M == 1:
    print(max(snack))
else:
    
    while left <= right:
    
        # print(left, right)
        # if right - left == 1:
        #     break
        
        mid = (left + right) // 2
        give = 0
        for i in range(len(snack)):
            give += (snack[i] // mid)
    
        if give < M: # 작게 나눠줘야함
            right = mid - 1 
        else:
            answer = mid
            left = mid + 1
    
    if answer == 0:
        print(0)
    else:
        print(answer)
            
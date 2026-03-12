T = int(input())
# 회문은 0, 유사회문 1, 그외 2

def hhh(get, left, right):
    while left < right:
        if get[left] == get[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

for i in range(T):
    get = list(input().strip())
    answer = 0

    left = 0
    right = len(get) - 1
    
    while left < right:
        if get[left] == get[right]:
            left += 1
            right -= 1
        else:
            checkL = hhh(get, left +1, right)
            checkR = hhh(get, left, right-1)
            if checkL or checkR:
                answer = 1
                break
            else:
                answer = 2
                break
    print(answer)
            
    
            
                
        
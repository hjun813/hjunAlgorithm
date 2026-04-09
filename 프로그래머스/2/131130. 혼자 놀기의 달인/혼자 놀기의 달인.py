def solution(cards):
    answer = 0
    leng = len(cards)
    check = [0 for _ in range(leng)]
    can = []
    
    def deep(i, n):
        check[i] = 1
        if check[cards[i] - 1] == 1:
            can.append(n)
            return
            
        deep(cards[i] - 1, n+1)
    
    for i in range(leng):
        if check[i] == 0:
            deep(i, 1)
    if len(can) == 1:
        answer = 0
    else:    
        a = max(can)
        can.remove(a)
        b = max(can)
        answer = a * b
    return answer
T = int(input())
for i in range(T):
    R, B, M = map(float, input().split())
    balance = int(B * 100 + 0.5)
    payment = int(M * 100 + 0.5)
    
    y = 0
    can = 0

    while balance > 0 :
        y += 1
        
        interest = int(balance * R / 100 + 0.5)
        
        balance += interest
        balance -= payment
        
        if y > 1200 :
            can = 1
            break

    if can == 0:
        print(y)
    else:
        print("impossible")
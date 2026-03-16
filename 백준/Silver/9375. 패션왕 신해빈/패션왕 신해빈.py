T = int(input())
for i in range(T):
    n = int(input())
    have = {}
    for j in range(n):
        name, category = input().split()
        
        if category in have:
            have[category] += 1
        else:
            have[category] = 1
    ans = 1
    for cnt in have.values():
        ans *= (cnt + 1)
    print(ans - 1)
    
    
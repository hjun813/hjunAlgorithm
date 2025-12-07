from itertools import combinations


n, m = map(int, input().split())

cardInfo = list(map(int, input().split()))
ans = 0



for i in combinations(cardInfo, 3):
    total = sum(i)
    if total <= m and total > ans:
        ans = total
        
        

print(ans)
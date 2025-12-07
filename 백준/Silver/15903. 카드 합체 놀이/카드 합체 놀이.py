import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
card = list(map(int, input().split()))

for i in range(m):
    card.sort()
    sumNum = card[0] + card[1]
    card[0] = sumNum
    card[1] = sumNum
 
answer = sum(card)

print(answer)

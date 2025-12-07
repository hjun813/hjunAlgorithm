import sys
input = sys.stdin.readline

k = int(input())
direction = []
mapLen = []
cnt = [0,0,0,0,0]
temp = 0
temp1 = 0
tempi = 0
tempi1 = 0
length = 0
lenngth2 = 0

for _ in range(6):
    d, l = map(int, input().split())
    direction.append(d)
    mapLen.append(l)
    
for i in range(6):
    a = direction[i]
    cnt[a] += 1

for j in range(5):
    if cnt[j] == 1:
        if temp == 0:
            temp = j
        else:
            temp1 = j

for i in range(6):
    if direction[i] == temp:
        length = mapLen[i]
        tempi = i
        break
    
for i in range(6):
    if direction[i] == temp1:
        length1 = mapLen[i]
        tempi1 = i
        break
if (tempi == 0 and tempi1 == 5) or (tempi == 5 and tempi1 == 0):
    need = 0
else : need = max(tempi1, tempi)
minus = mapLen[(need + 2) % 6] * mapLen[(need + 3) % 6]

print(((length * length1) - minus) * k)
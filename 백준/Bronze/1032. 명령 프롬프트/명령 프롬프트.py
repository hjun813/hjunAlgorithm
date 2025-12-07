N = int(input())
check = []
for i in range(N):
    temp = list(input().strip())
    check.append(temp)

for i in range(len(check[0])):
    temp = check[0][i]
    for j in range(1, N):
        if temp != check[j][i]:
            check[0][i] = '?'
            break

for i in range(len(check[0])):
    print(check[0][i], end='')
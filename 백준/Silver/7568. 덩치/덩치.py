N = int(input())
get = []
ans = []
for i in range(N):
    x, y = map(int, input().split())
    get.append([x, y])

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if get[i][0] < get[j][0] and get[i][1] < get[j][1]:
                rank += 1
    ans.append(rank)

print(*ans)
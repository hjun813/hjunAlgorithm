from itertools import combinations 

N, S = map(int, input().split())
num = list(map(int, input().split()))
count = 0

for i in range(1, N+1):
    comb = combinations(num, i) # num의 리스트에서 i 개의 조합 찾기 ()

    for j in comb:
        if sum(j) == S:
            count += 1

print(count)
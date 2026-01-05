K = int(input())
for k in range(K):
    M, N, P = map(int, input().split()) # M: 문제의 수, N: 총 제출 수, P: 참가자의 수
    print("Data Set", end=" ")
    print(k+1, end="")
    print(":")

    # 문제 저장
    check = [[0 for _ in range(M)] for _ in range(P)]
    solve = [0 for _ in range(P)]
    total = [0 for _ in range(P)]
    rank = []
    
    for n in range(N):
        p, m, t, j = input().split() # p: 제출한 참가자, m: 문제 번호, t: 제출한 시각, j: 정답 여부
        p = int(p) - 1
        t = int(t)
        j = int(j)
        m = ord(m) - 65
        if check[p][m] != -1:
            if j == 0: # 오답일 경우
                check[p][m] += 1
            else: # 정답일 경우
                total[p] += (t + check[p][m] * 20)
                check[p][m] = -1
                solve[p] += 1
    for d in range(P):
        rank.append([-solve[d], total[d], d+1])
    rank.sort()
    for d in range(P):
        print(rank[d][2], -rank[d][0], rank[d][1])
    if k != K-1:
        print()
        
            
        
        
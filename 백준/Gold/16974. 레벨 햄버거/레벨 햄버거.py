N, X = map(int, input().split())
answer = 0
# 약간 프랙탈 구조
# N0 = P (1)(1, 0)
# N1 = B(N0)P(N0)B =  PBBBP (5)(3, 2)
# N2 = B (N1) P (N1) B (13) (7, 4)
# N3 = N3 = B (N2) P (N2) B = B B (N1) P (N1) B P B (N1) P (N1) B B
# 그럼 최대 50 까지
# 다 만드는건 오바고
# A(n) = 2 * A(n-1) + 3
# A(1) = 1
# A(n) = 2 * 2 ^ N - 3 : 개수
# 패티 - 2 * N - 1
# 빵 - 2 * (N-1)

def hambu(n, i): # n 번째 버거, i 인덱스
    
    if n == 0 :
        return 1
    if n == 1:
        patte = 1
        ham = 0
    else:
        patte = 2 ** (n-1) - 1
        ham = 2 ** n - 3
        
    if n == 1 and i == 1:
        return 1
        
    if  i == 2 * ham + 3: # 첫 햄버거 빵
        return 2 * patte + 1
    elif ham + 2 < i < 2 * ham + 3: # 그 사이 앞의 버거
        return hambu(n-1, i-2-ham) + 1 + patte
    elif i == ham + 2: # 그사이 패티
        return patte + 1
    elif 1 < i < ham + 2: # 그 사이 뒤의 버거
        return hambu(n-1, i-1)
    elif i == 1: # 마지막 햄버거 빵
        return 0
        
print(hambu(N+1, X))

        
    

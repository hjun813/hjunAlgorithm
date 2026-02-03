N, M, K = map(int, input().split())

# N개 중에 M개 있는데 K개 뒤졌을때
# 한개 이상이니까
# 없는 확률을 빼자

Boom = N - M

for i in range(K):
    answer = 1
    for j in range(1, i+2):
        answer = answer * ((Boom - j + 1) / (N - j + 1))
    print(format(1 - answer, '.10f'))

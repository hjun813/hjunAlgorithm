D, K = map(int, input().split())
# D-1 번째 피보나치 수 구하기

a = 1
b = 1

for i in range(D-3):
    t = b
    b += a
    a = t

idx = 0

while True:
    idx += 1
    if (K - idx * a) % b == 0:
        print(idx)
        print((K - idx * a) // b)
        break

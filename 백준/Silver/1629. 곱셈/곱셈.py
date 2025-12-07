import sys

A, B, C = map(int, sys.stdin.readline().split())

x = A % C


# def restFunction(a, b, c):

#     if b > 1: 
#         if b % 2 == 0:
#             return (restFunction(a, b // 2, c) * restFunction(a, b // 2, c)) % c
#         elif b % 2 == 1:
#             return (restFunction(a, (b - 1) // 2, c) * restFunction(a, (b - 1) // 2, c) * (a % c)) % c
#     elif b == 1:
#         return a % c
    
# print(restFunction(x, B, C))

print(pow(x, B, C))
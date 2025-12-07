import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
vowcheck = ['a', 'e', 'i', 'o', 'u']
alphabet.sort()

possible = list(combinations(alphabet, L))
for check in possible:
    cnt = 0
    for element in check:
        if element in vowcheck:
            cnt += 1
    if cnt > 0 and L - cnt > 1:
        for i in range(L):
            print(check[i], end="")
        print()
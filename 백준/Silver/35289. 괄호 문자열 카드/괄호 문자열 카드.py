import sys

A, B, C, D, E, F = map(int, sys.stdin.readline().split())

total_in = A + 2 * B
total_out = C + 2 * D

M = min(total_in, total_out)

if A == 0 and M % 2 == 1:
    M -= 1
if C == 0 and M % 2 == 1:
    M -= 1

answer = 2 * M + 2 * E

if M > 0:
    answer += 2 * F

print(answer)
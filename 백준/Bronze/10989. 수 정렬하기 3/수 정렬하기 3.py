import sys

num = int(input())
test = [0] * (10001)

for i in range(num):
    test[int(sys.stdin.readline())] += 1

for i in range(10001):
    for j in range(int(test[i])):
        sys.stdout.write(str(i) + "\n")
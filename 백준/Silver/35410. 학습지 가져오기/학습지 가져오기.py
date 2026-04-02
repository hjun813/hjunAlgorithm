N = int(input())
time = list(map(int, input().split()))
time.sort()
answer = 0
i = 0

while i != N:
    
    answer += 1

    if answer >= time[i]:
        i += 1
        continue

print(answer+1)

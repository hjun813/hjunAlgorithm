N, T = map(int, input().split())
Info = []
result = []
bf = 0

for i in range(N):
    name, length = input().split()
    bf += int(length)
    Info.append([bf % T, name])

Info.sort()

for i in range(N):
    if i == 0:
        # 맨 앞이랑 비교
        if T + Info[i][0] - Info[-1][0] <= 1000:
            result.append(Info[i][1])
    else:
        if Info[i][0] - Info[i-1][0] <= 1000:
            result.append(Info[i][1])


if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in range(len(result)):
        print(result[i])
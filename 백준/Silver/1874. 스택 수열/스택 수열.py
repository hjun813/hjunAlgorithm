N = int(input())
check = []
get = []
answer = []

for i in range(N):
    t = int(input())
    check.append(t)

j = 0
for i in range(1, N+1):

    get.append(i)
    answer.append('+')

    while True:
        if len(get) > 0:
            if get[-1] == check[j]:
                get.pop()
                answer.append('-')
                j += 1
            else:
                break
        else:
            break
if j != N:
    print("NO")
else:
    for i in range(len(answer)):
        print(answer[i])

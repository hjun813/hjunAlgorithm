n, L = map(int, input().split())
box = list(map(int, input().split()))

before = 0
cnt = 0
answer = "stable"

for i in range(n-1, 0, -1):
    avg = (before * cnt + box[i]) / (cnt+1)
    s = box[i-1] - L
    e = box[i-1] + L

    if s < avg < e:
        before = avg
        cnt += 1
        continue
    else:
        answer = "unstable"
        break

print(answer)
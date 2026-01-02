n = int(input())
santa = []

for i in range(n):
    next = input()
    if next == '0':
        if len(santa) == 0:
            print("-1")
        else:
            give = santa.pop()
            print(give)
    else:
        info = list(map(int, next.split()))
        for k in range(1, len(info)):
            santa.append(info[k])
        santa.sort()
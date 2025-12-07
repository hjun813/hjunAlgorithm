import sys

n = int(sys.stdin.readline())
circle_info = []
stack = []
count = 1

for i in range(n):
    r, c = list(map(int, sys.stdin.readline().split()))
    circle_info.append([r - c, "("])
    circle_info.append([r + c, ")"])

circle_info.sort(key=lambda x: (x[0], -ord(x[1])))

for i in range(n * 2):

    if stack:
        if circle_info[i][1] == "(" and circle_info[i][0] == stack[-1]["pos"]:

            stack[-1]["state"] = 2

        elif circle_info[i][1] == ")":
            count += stack.pop()["state"]

            if not stack:
                continue

            if i + 1 < 2 * n and circle_info[i + 1][0] != circle_info[i][0]:
                stack[-1]["state"] = 1
            continue

    stack.append({"pos": circle_info[i][0], "shape": circle_info[i][1], "state": 1})

print(count)
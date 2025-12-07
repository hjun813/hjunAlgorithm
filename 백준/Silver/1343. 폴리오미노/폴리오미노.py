import sys
input = sys.stdin.readline
boardMap = input().rstrip()
boardMap = boardMap.replace("XXXX", "AAAA")
boardMap = boardMap.replace("XX", "BB")


if "X" in boardMap:
    print(-1)
else:
    print(boardMap)
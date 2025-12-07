import sys

side = int(sys.stdin.readline())
paper = [0] * side
num = 0
blueCheck = 0
whiteCheck = 0

for i in range(side):
    paper[i] = list(map(int, sys.stdin.readline().split()))


def divide(n, a, b):  # a,b가 시작점

    global blueCheck
    global whiteCheck
    
    color = paper[a][b]
    nextSide = int(n/2)
   
    for i in range(a, a + n):
        for j in range(b, b + n):
            if paper[i][j] != color:
                divide(nextSide, a, b)
                divide(nextSide, a, b + (nextSide))
                divide(nextSide, a + (nextSide), b)
                divide(nextSide, a + (nextSide), b + (nextSide))
                return
    if color == 0:
        whiteCheck += 1
    else:
        blueCheck += 1


divide(side, 0 ,0)
print(whiteCheck)
print(blueCheck)
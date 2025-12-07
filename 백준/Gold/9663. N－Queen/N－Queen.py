num = int(input())
nQueenPos = [0] * num
nQueenPosHor = [False] * num
nQueenPostive = [False] * (num * 2 - 1)
nQueenNegative = [False] * (num * 2 - 1)
count = 0


def nQueen(num, n):
    global count
    if n < num:

        for i in range(num):

            if not nQueenPosHor[i] and not nQueenPostive[n + i] and not nQueenNegative[n - i + num - 1]:
                nQueenPos[n] = i
                
                nQueenPosHor[i] = True
                nQueenPostive[n + i] = True
                nQueenNegative[n - i + num - 1] = True
                nQueen(num, n + 1)
                nQueenPosHor[i] = False
                nQueenPostive[n + i] = False
                nQueenNegative[n - i + num - 1] = False

    elif n == num:
        # print(nQueenPos)
        count = count+1


nQueen(num, 0)
print(count)

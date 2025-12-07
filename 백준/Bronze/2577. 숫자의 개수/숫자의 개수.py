A = int(input())
B = int(input())
C = int(input())

multNum = A * B * C


multNumList = list(map(int, str(multNum)))
for i in range(10):
    print(multNumList.count(i))
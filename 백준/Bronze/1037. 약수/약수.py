n = int(input())
yacsu = list(map(int, input().split()))
yacsu.sort()

answer = yacsu[0] * yacsu[-1]
print(answer)
    

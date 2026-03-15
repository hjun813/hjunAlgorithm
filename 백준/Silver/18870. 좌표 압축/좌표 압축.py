import sys
input = sys.stdin.readline

N = int(input())
get = list(map(int, input().split()))

get2 = list(set(get))
get2.sort()
dic = {val : i for i , val in enumerate(get2)}

for i in range(N):
    print(dic[get[i]], end=" ")
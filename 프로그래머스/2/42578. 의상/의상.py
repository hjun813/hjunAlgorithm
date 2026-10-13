from collections import defaultdict

def solution(clothes):
    answer = 1
    check = defaultdict(int)
    for i in range(len(clothes)):
        check[clothes[i][1]] += 1
    for count in check.values():
        answer *= (count + 1)
    return answer - 1
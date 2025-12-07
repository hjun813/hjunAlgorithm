N = int(input())
peopleNum = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for i in range(len(peopleNum)):
    
    check = peopleNum[i]
    check -= B
    answer += 1
    if(check <= 0):
        continue
    else:
        a = check // C
        b = check % C
        if(b > 0):
            answer += (a + 1)
        else:
            answer += a
print(answer)
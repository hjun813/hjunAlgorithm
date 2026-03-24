get = list(input())
temp = 0
answer = 0
i = 0

while i < len(get):
    
    if i != len(get) - 1:
        if get[i] == '(' and get[i+1] == ')':
            answer += temp
            i += 2
        else:
            if get[i] == '(':
                temp += 1
                i += 1
            else:
                temp -= 1
                answer += 1
                i += 1
    elif i == len(get) - 1:
        answer += temp
        i+= 1

print(answer)
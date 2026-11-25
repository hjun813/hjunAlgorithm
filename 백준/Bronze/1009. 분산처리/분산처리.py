T= int(input())
for t in range(T):
    a,b = map(int, input().split())
    # a**b 의 마지막 숫자만 알면 되는거 같은디
    check = b % 4
    answer = 0
    # a = 1이면 무조건 1
    a = a % 10
    if a == 1:
        answer = 1
    # 2 이면 2, 4, 8, 6 순서
    elif a == 2:
        if check == 1:
            answer = 2
        elif check == 2:
            answer = 4
        elif check == 3:
            answer = 8
        else:
            answer = 6
    # 3 이면 3, 9, 7, 1 순서
    elif a == 3:
        if check == 1:
            answer = 3
        elif check == 2:
            answer = 9
        elif check == 3:
            answer = 7
        else:
            answer = 1
    # 4 이면 4, 6, 4, 6 반복
    elif a == 4:
        if check == 1 or check == 3:
            answer = 4
        else:
            answer = 6
    # 5 이면 무조건 5
    elif a == 5:
        answer = 5
    # 6 이면 무조건 6
    elif a == 6:
        answer = 6
    # 7 이면 7, 9, 3, 1
    elif a == 7:
        if check == 1:
            answer = 7
        elif check == 2:
            answer = 9
        elif check == 3:
            answer = 3
        else:
            answer = 1
    # 8 이면 8, 4, 2, 6
    elif a == 8:
        if check == 1:
            answer = 8
        elif check == 2:
            answer = 4
        elif check == 3:
            answer = 2
        else:
            answer = 6
    # 9 이면 9, 1, 9, 1 반복
    elif a == 9:
        if check == 1 or check == 3:
            answer = 9
        else:
            answer = 1
    # 0 이면 무조건 10
    else:
        answer = 10

    print(answer)


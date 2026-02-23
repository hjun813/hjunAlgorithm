T = int(input())
for i in range(T):
    testcase = list(map(int, input().strip()))
    idx = 0
    lenTest = len(testcase)
    answer = "YES"

    while idx < lenTest:
        flag = 1
        if testcase[idx] == 0:
            if idx + 1 < lenTest:
                if testcase[idx + 1] == 1:
                    flag = 0
                    idx += 2
                    continue

        if testcase[idx] == 1:
            temp0 = 0
            temp1 = 0
            while idx + temp0 + 1 < lenTest and testcase[idx + temp0 + 1] == 0:
                temp0 += 1
            idx += temp0
            while idx + temp1 + 1 < lenTest and testcase[idx + temp1 + 1] == 1:
                temp1 += 1
            idx += temp1

            if idx + 2 < lenTest:
                    if testcase[idx + 1] == 0 and testcase[idx + 2] == 0:
                        temp1 -= 1
                        idx -= 1
            if temp0 >= 2 and temp1 >= 1:
                flag = 0
                idx += 1
                continue

        if flag == 1:
            answer = "NO"
            break
            
    print(answer)
                
        
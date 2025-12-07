testcase_num = int(input())
testcase = list()


for i in range(testcase_num):
    testcase.append(str(input()))
    score = 0
    a = testcase[i].split("X")
    
    for j in range(len(a)):
        for k in range(len(a[j])):
            score = score + (k + 1)

    print(score)

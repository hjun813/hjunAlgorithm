def solution(id_list, report, k):
    # k번 이상 신고 당하면 정지
    # 내가 신고한놈 정지되면 알림받음
    # 똑같은 놈은 신고 불가
    
    # 이차원 배열 만들고 신고 추적하고

    n = len(id_list)
    answer = [0 for _ in range(n)]
    check = [0 for _ in range(n)]
    report_l = [[0 for _ in range(n)] for _ in range(n)]
    id_dic = {name : i for i, name in enumerate(id_list)}
    
    for i in range(len(report)):
        good, bad = report[i].split()
        goodIdx = id_dic[good]
        badIdx = id_dic[bad]
        if report_l[badIdx][goodIdx] == 0:
            report_l[badIdx][goodIdx] += 1
            check[badIdx] += 1
    
    for i in range(n):
        if check[i] >= k:
            for j in range(n):
                if report_l[i][j] == 1:
                    answer[j] += 1
    return answer
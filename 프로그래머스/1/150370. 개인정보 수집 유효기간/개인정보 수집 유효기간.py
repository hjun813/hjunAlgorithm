def solution(today, terms, privacies):
    answer = []
    t_year, t_month, t_day = map(int, today.split('.'))
    today_int = (t_year * 12 + t_month) * 28 + t_day
    terms_dic = {}
    for i in range(len(terms)):
        t_p, t_l = terms[i].split()
        t_l = int(t_l)
        terms_dic[t_p] = t_l
    
    for i in range(len(privacies)):
        get, p = privacies[i].split()
        get_year, get_month, get_day = map(int, get.split('.'))
        get_int = (get_year * 12 + get_month) * 28 + get_day
        get_int += terms_dic[p] * 28
        if today_int >= get_int:
            answer.append(i+1)
    return answer
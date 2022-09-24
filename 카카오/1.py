# 매 달은 28일까지만 있음
def solution(today, terms, privacies):
    answer = []
    n_terms = {}
    n_priv = []

    st_year, st_month, st_day = today.split(".")
    t_year, t_month, t_day = int(st_year), int(st_month), int(st_day)

    for i in terms:
        a, b = i.split(" ")
        n_terms[a] = b

    for i in privacies:
        a, b = i.split(" ")
        n_priv.append([a,b])

    today_ym = (t_year - 2000) * 12 + t_month
    print(today_ym)
    for i in range(len(n_priv)):
        yak = n_priv[i][1]
        days = int(n_terms[yak])

        s_year, s_month, s_day = n_priv[i][0].split(".")
        year, month, day = int(s_year), int(s_month), int(s_day)

        month += days
        now_ym = (year-2000) * 12 + month
        print(now_ym)

        if now_ym < today_ym:
            answer.append(i+1)
        elif now_ym == today_ym and day <= t_day:
            answer.append(i+1)

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
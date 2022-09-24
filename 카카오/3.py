def solution(users, emoticons):
    answer = []
    sales = [0.4] * len(emoticons)

    total = 0
    cnt = 0

    for i in range(len(users)):
        money = 0
        for j in range(len(emoticons)):
            if sales[j] >= users[i][0] * 0.01:
                money += emoticons[j] * (1-sales[j])

        if money < users[i][1]:
            total += money
        else:
            cnt += 1

    answer.append(cnt)
    answer.append(int(total))
    return answer


print(solution([[40,2900], [23,10000], [11,5200], [5,5900], [40,3100], [27,9200], [32,6900]], [1300,1500,1600,4900]))
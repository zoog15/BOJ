def solution(a, b):
    months = [29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    days = 0
    if a > 1:
        days += 31
        for i in range(0, a-2):
            days += months[i]
        days += b
    else:
        days += b

    print(days)

    answer = day[days%7]
    return answer


print(solution(3,1))
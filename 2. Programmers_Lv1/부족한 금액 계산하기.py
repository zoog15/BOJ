def solution(price, money, count):
    first = price

    for i in range(0, count):
        money -= price
        price += first

    if money >= 0:
        return 0
    else:
        return money*-1


print(solution(3,20,4))
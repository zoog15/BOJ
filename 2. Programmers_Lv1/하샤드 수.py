def solution(x):
    str_x = str(x)
    hashad = 0

    for i in str_x:
        hashad += int(i)

    if x % hashad == 0:
        return True
    else:
        return False


print(solution(10))
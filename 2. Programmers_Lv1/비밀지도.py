def ezin(num, n):
    two_num = ''

    while True:
        if num == 0:
            break
        two_num += str(num%2)
        num //= 2

    if len(two_num) != n:
        while len(two_num) != n:
            two_num += '0'

    return two_num


def solution(n, arr1, arr2):
    sol = []

    for i in range(n):
        map1 = ezin(arr1[i], n)
        map2 = ezin(arr2[i], n)
        s = ''
        for j in range(n):
            if map1[j] == '0' and map2[j] == '0':
                s += ' '
            else:
                s += '#'

        new_s = ''
        for i in range(n):
            new_s += s[n-i-1]
        sol.append(new_s)

    return sol


print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
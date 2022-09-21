import math


def sosu(n):
    answer = 0
    sosus = [True for i in range(n+1)]

    if n == 2:
        return 1

    for i in range(2, int(math.sqrt(n))+1):
        if sosus[i]:
            j = 2
            while i*j <= n:
                sosus[i*j] = False
                j += 1

    for i in range(n//2+1, n+1):
        if sosus[i]:
            answer += 1

    return answer


while True:
    n = int(input())
    if n == 0:
        break

    print(sosu(2*n))


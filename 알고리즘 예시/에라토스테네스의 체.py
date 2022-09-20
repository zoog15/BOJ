import math


def solution(n):
    answer = 0

    # 에라토스테네스의 체 초기화: n 개 요소에 True 설정(일단 소수로 간주)
    sosu = [True for i in range(n + 1)]

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if sosu[i]: # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                sosu[i*j] = False
                j += 1

    for i in range(2, n + 1):
        if sosu[i]:
            answer += 1

    return answer
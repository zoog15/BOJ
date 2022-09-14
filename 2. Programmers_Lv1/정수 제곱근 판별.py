import math

def solution(n):
    answer = 0
    if math.sqrt(n) == int(math.sqrt(n)):
        a = int(math.sqrt(n)) + 1
        answer = pow(a,2)
    else:
        answer = -1
    return answer


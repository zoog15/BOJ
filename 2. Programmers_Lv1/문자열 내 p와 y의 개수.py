def solution(s):
    s = s.lower()

    y = s.count('y')
    p = s.count('p')

    return y == p


print(solution("pPoooyY"))
print(solution("Pyy"))
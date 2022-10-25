def solution(a):
    if a == 1:
        return 1
    if a == 2:
        return 2
    if a == 3:
        return 4

    return solution(a-3) + solution(a-2) + solution(a-1)


n = int(input())

for i in range(n):
    a = int(input())
    print(solution(a))
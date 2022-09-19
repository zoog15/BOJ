def solution(sizes):
    max_a, max_b = 0, 0

    for i in range(len(sizes)):
        # a는 두변중 긴변들만, b는 두변중 작은 변들만 모아놓는다고 생각
        a = max(sizes[i][0], sizes[i][1])
        b = min(sizes[i][0], sizes[i][1])

        max_a = max(max_a, a)
        max_b = max(max_b, b)

    return max_a*max_b


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
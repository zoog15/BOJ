def solution(d, budget):
    d.sort()
    budget_sum = 0
    cnt = 0
    for i in d:
        budget_sum += i
        if budget_sum > budget:
            break
        else:
            cnt += 1

    return cnt


print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))
def solution(n):
    memo = [0] * 100

    # 1층이나 2층은 1번에 바로 갈수있음
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    print(memo)
    return memo[n]


print(solution(2))
print(solution(3))
print(solution(10))
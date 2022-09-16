from collections import deque


def solution(arr):
    answer = [arr[0]]

    d_arr = deque(arr)

    for i in range(len(d_arr)):
        pop_n = d_arr.popleft()
        if answer[-1] != pop_n:
            answer.append(pop_n)

    return answer


print(solution([1,1,3,3,0,1,1]))
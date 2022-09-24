from typing import List


def solution(queries: List[List[int]]) -> int:
    answer = 0

    lists = {}
    index = {}
    second = [1,2,4,8,16,32,64,128,256,512, 1024, 2048, 5096]

    for i in range(len(queries)):
        if queries[i][0] in lists:
            new = lists.get(queries[i][0]) + queries[i][1]
            i_start = index.get(queries[i][0])
            for j in range(i_start, len(second)):
                if new >= second[j]:
                    answer += lists.get(queries[i][0])
                    break
            lists[queries[i][0]] = new
        else:
            lists[queries[i][0]] = queries[i][1]
            for j in second:
                if queries[i][1] <= j:
                    index[queries[i][0]] = second.index(j)
                    break

    return answer


print(solution([[2,10], [7,1], [2,5], [2,9], [7,32]]))
print(solution([[1,1], [1,2], [1,4], [1,8]]))
from typing import List
import math


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[]]

    map = [[0 for _ in range(n)] for _ in range(n)]
    fire_effect = [[0 for _ in range(n)] for _ in range(n)]
    ice_effect = [[0 for _ in range(n)] for _ in range(n)]


    print(map, fire_effect, ice_effect)

    return answer


print(solution(3,2,[[1,1]], [[3,3]]))
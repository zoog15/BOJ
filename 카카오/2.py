def solution(cap, n, deliveries, pickups):
    answer = 0

    deliveries.reverse()
    pickups.reverse()

    while True:
        if sum(deliveries) + sum(pickups) == 0:
            break


    return answer


print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))
print(solution(2,7,[1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))
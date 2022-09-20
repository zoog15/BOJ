def solution(N, stages):
    failure_rate = {}
    stages_len = len(stages)

    for i in range(1, N+1):
        # stages_len이 0이되면 모든 유저의 스테이지가 계산됏으니, 나머지 쓸데없는 연산을 줄일수 있음
        if stages_len != 0:
            stage_count = stages.count(i)
            # 실패율 바로 소숫점으로 넣기
            failure_rate[i] = stage_count/stages_len
            stages_len -= stage_count
        else:
            failure_rate[i] = 0

    # 람다식 정렬방법
    answer = sorted(failure_rate.keys(), key=lambda key: failure_rate[key], reverse=True)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
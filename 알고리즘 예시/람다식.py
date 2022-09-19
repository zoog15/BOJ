def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])

# 이런식으로 하면 string에서 string[n]을 기준으로 정렬함
def solution(answers):
    answer = []

    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]

    length = len(answers)

    ns1 = s1*(length//len(s1))
    for i in range(length%len(s1)):
        ns1.append(s1[i])
    ns2 = s2*(length//len(s2))
    for i in range(length%len(s2)):
        ns2.append(s2[i])
    ns3 = s3*(length//len(s3))
    for i in range(length%len(s3)):
        ns3.append(s3[i])

    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(length):
        if answers[i] == ns1[i]:
            cnt1 += 1
        if answers[i] == ns2[i]:
            cnt2 += 1
        if answers[i] == ns3[i]:
            cnt3 += 1

    max_s = max(cnt1, cnt2, cnt3)

    if cnt1 == max_s:
        answer.append(1)
    if cnt2 == max_s:
        answer.append(2)
    if cnt3 == max_s:
        answer.append(3)

    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
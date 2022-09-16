def solution(s):
    list_s = s.split(" ")
    temp2 = []
    for i in range(len(list_s)):
        l = list(list_s[i])
        temp = ''
        for j in range(len(l)):
            if j % 2 == 0:
                temp += l[j].upper()
            else:
                temp += l[j].lower()
        temp2.append(temp)

    answer = ' '.join(temp2)

    return answer


print(solution("try hello world"))
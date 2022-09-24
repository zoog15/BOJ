def solution(a,b):
    len_a = len(a)
    len_b = len(b)

    int_a = 0
    int_b = 0
    for i in range(len_a):
        int_a += int(a[i]) * pow(2,len_a-i-1)

    for i in range(len_b):
        int_b += int(b[i]) * pow(2, len_b-i-1)

    final = int_a + int_b

    return format(final, 'b')



print(solution("11", "1"))
print(solution("1010", "1011"))
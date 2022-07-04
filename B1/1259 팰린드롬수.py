while True:
    n = input()
    if n == '0':
        break

    flag = 0
    cen = len(n)//2

    # 길이가 홀수일때
    if len(n)%2 == 1:
        for i in range(cen):
            if n[cen-i-1] != n[cen+i+1]:
                flag = 1
                break
    # 길이가 짝수일때
    else:
        for i in range(cen):
            if n[cen-i-1] != n[cen+i]:
                flag = 1
                break
    if flag == 0:
        print("yes")
    else:
        print("no")
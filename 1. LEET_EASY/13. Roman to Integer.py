def romanToInt(s):
    length = len(s)
    ans = 0
    flag = 0

    for i in range(length):
        if flag == 1:
            flag = 0
            continue

        if s[i] == 'I':
            ans += 1
            if i < length - 1:
                if s[i + 1] == 'V':
                    ans += 3
                    flag = 1
                elif s[i + 1] == 'X':
                    ans += 8
                    flag = 1
        elif s[i] == 'V':
            ans += 5
        elif s[i] == 'X':
            ans += 10
            if i < length - 1:
                if s[i + 1] == 'L':
                    ans += 30
                    flag = 1
                elif s[i + 1] == 'C':
                    ans += 80
                    flag = 1
        elif s[i] == 'L':
            ans += 50
        elif s[i] == 'C':
            ans += 100
            if i < length - 1:
                if s[i + 1] == 'D':
                    ans += 300
                    flag = 1
                elif s[i + 1] == 'M':
                    ans += 800
                    flag = 1
        elif s[i] == 'D':
            ans += 500
        elif s[i] == 'M':
            ans += 1000

    return ans


print(romanToInt("MCMXCIV"))

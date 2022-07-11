while True:
    s = input()
    if s == '#':
        break
    low_s = s.lower()
    sum = 0
    sum += low_s.count('a')
    sum += low_s.count('e')
    sum += low_s.count('i')
    sum += low_s.count('o')
    sum += low_s.count('u')

    print(sum)
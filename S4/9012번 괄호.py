n = int(input())

for i in range(n):
    stack = list(input())
    temp = []

    for i in stack:
        if i == '(':
            temp.append(i)
        else:
            if temp and temp[-1] == '(':
                temp.pop()
            else:
                temp.append(i)

    if temp:
        print("NO")
    else:
        print("YES")
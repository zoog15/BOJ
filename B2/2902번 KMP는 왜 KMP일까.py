s = input()

ans = []

for i in s:
    if i.isupper():
        ans.append(i)

for i in ans:
    print(i, end='')
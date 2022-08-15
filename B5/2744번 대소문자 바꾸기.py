s = input()
new_s = []
for i in s:
    if i.isupper():
        new_s.append(i.lower())
    if i.islower():
        new_s.append(i.upper())

for i in new_s:
    print(i, end='')
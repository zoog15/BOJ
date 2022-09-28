s = input()

bubun = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        temp = s[i:j+1]
        bubun.add(temp)

print(len(bubun))



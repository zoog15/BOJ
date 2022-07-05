s = input()

words = [0 for _ in range(26)]
# a = 97

for i in s:
    index = ord(i)-97
    words[index] += 1

print(*words)

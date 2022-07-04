# 숫자 몇개
n = int(input())

words = []
for i in range(n):
    s = input()
    if s not in words:
        words.append(s)

words.sort()
words.sort(key = len)

for i in words:
    print(i)
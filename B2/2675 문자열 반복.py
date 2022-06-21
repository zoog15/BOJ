n = int(input())

for i in range(n):
    repeat, words = map(str, input().split())
    l_words = list(words)
    for j in range(len(l_words)):
        print(l_words[j]*int(repeat), end="")
    print()
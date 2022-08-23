s = input()
half = len(s)//2

isFelin = 0
if len(s)%2 == 0:
    for i in range(1, half+1):
        if s[half+i-1] != s[half-i]:
            isFelin = 1
else:
    for i in range(1, half+1):
        if s[half-i] != s[half+i]:
            isFelin = 1

if isFelin == 1:
    print(0)
else:
    print(1)
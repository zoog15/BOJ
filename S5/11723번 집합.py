
ans = set()
n = int(input())

for i in range(n):
    s = input()
    if " " in s:
        func, a = s.split(" ")

        if func == "add":
            if a not in ans:
                ans.add(a)
        elif func == "remove":
            if a in ans:
                ans.remove(a)
        elif func == "check":
            if a in ans:
                print(1)
            else:
                print(0)
        elif func == "toggle":
            if a in ans:
                ans.remove(a)
            else:
                ans.add(a)
    else:
        func = s

        if func == "all":
            ans.clear()
            for i in range(1, 21):
                ans.add(i)
        elif func == "empty":
            ans.clear()
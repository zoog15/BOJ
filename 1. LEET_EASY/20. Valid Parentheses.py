s = input()

stack = []

for i in s:
    if i == '(':
        stack.append(i)
    elif i == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)

    if i == '[':
        stack.append(i)
    elif i == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(i)

    if i == '{':
        stack.append(i)
    elif i == '}':
        if stack and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(i)

if stack:
    print("false")
else:
    print("true")

print(stack)
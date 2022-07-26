people = 0
max_people = 0

for i in range(4):
    a, b = map(int, input().split())
    people -= a
    people += b

    if people >= max_people:
        max_people = people

print(max_people)
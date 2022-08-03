science = []
society = []

science.append(int(input()))
science.append(int(input()))
science.append(int(input()))
science.append(int(input()))

society.append(int(input()))
society.append(int(input()))

science.remove(min(science))
society.remove(min(society))

print(sum(science) + sum(society))


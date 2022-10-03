n = int(input())

weight = []
for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)

result = []
for i in range(n):
    result.append(weight[i]*(i+1))

print(max(result))
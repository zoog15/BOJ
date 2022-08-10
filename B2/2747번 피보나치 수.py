n = int(input())

pibo = [0,1,1]

for i in range(3,n+1):
    new_pibo = pibo[i-1] + pibo[i-2]
    pibo.append(new_pibo)

print(pibo[n])
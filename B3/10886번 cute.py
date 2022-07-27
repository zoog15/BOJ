people = int(input())
one_cnt = 0
zero_cnt = 0

for i in range(people):
    cute = int(input())
    if cute == 1:
        one_cnt += 1
    if cute == 0:
        zero_cnt += 1

if one_cnt > zero_cnt:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
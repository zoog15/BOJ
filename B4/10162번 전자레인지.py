a = 300
b = 60
c = 10

time = int(input())

a_cnt = time // 300

time -= a_cnt * 300

b_cnt = time // 60

time -= b_cnt * 60

c_cnt = time // 10

time -= c_cnt*10

if time != 0:
    print(-1)
else:
    print(a_cnt, b_cnt, c_cnt)


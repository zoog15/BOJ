x, y, w, h = map(int, input().split())

half_w = w/2
half_h = h/2

if x > half_w:
    ans_x = w-x
else:
    ans_x = x

if y > half_h:
    ans_y = h-y
else:
    ans_y = y

if ans_x > ans_y:
    print(ans_y)
else:
    print(ans_x)
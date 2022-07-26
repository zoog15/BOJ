for i in range(3):
    points = list(map(int, input().split()))
    if points.count(0) == 0:
        print("E")
    elif points.count(0) == 1:
        print("A")
    elif points.count(0) == 2:
        print("B")
    elif points.count(0) == 3:
        print("C")
    elif points.count(0) == 4:
        print("D")

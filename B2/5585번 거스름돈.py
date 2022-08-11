money = int(input())

change = 1000 - money
count = 0

while True:
    if change >= 500:
        count += change // 500
        change %= 500
    elif change >= 100:
        count += change // 100
        change %= 100
    elif change >= 50:
        count += change // 50
        change %= 50
    elif change >= 10:
        count += change // 10
        change %= 10
    elif change >= 5:
        count += change // 5
        change %= 5
    else:
        count += change
        break

print(count)
'''
    카운터에서 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전히 무한히 존재한다고 가정
    손님에게 거슬러 줘야 할 돈이 N원ㅇ리 때 거슬러 줘야할 동전의 최소 개수 구하기
    -> 가장 큰 화폐 단위부터 돈을 거술러 주는 것이 포인트
'''

n = 1260
count = 0

# 큰 단우의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬로 줄 수 있는 동전의 갯수 섹
    n %= coin

print(count)
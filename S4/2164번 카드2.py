from collections import deque

n = int(input())

queue = []

for i in range(1, n+1):
    queue.append(i)

d_queue = deque(queue)

while True:
    if len(d_queue) == 1:
        break
    # 제일 위 숫자 버리기
    d_queue.popleft()
    # 그다음 맨 앞에 있는 숫자 뒤로 보내기
    d_queue.append(d_queue.popleft())

print(*d_queue)

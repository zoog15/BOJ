from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visit_list[n] = 1
    count = 0

    while q:
        count += 1
        v = q.popleft()
        for i in range(1, computer + 1):
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

    return count - 1


computer = int(input())
n = int(input())

graph = [[0] * (computer+1) for _ in range(computer+1)]
visit_list = [0] * (computer+1)

for i in range(n):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

print(bfs(1))

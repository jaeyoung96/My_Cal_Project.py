# 미래 도시(플로이드 워셜 방법 사용)
INF = int(1e9)

n, m = map(int, input().split())
graph =[[INF] * (n + 1) for _ in range(n + 1)]
for a in range(n + 1):
    for b in range(n + 1):
         if a == b:
             graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

if graph[1][k] or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])
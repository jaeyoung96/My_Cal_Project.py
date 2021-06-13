#전보
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
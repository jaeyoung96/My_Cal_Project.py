from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#
def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        print('x, y = ',x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))
                print('q = ',q)
                print('graph[',nx,'][',ny,']',' = ',graph[nx][ny])
    return graph[n-1][m-1]

print('\n',bfs(0, 0),'\n')
for x in range(n):
    print(graph[x])

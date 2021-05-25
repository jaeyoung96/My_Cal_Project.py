from collections import deque
import time
import numpy as np

N,M = map(int, input().split()) # N : 세로, M : 가로
# ice_case = [[int(col) for col in input().split()]for row in range(M)]
# ice_case = np.random.randint(0,2,(N,M))
ice_case = []
for i in range(N):
    ice_case.append(list(map(int, input())))
print(ice_case)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x, y):
    que = deque()
    que.append((x,y))
    if ice_case[x][y] == 1:
        return False

    while que:
        x,y = que.popleft()
        ice_case[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and ice_case[nx][ny] == 0:
                que.append((nx,ny))
        print(x,y)

    return True

start_time = time.time()
count = 0

for i in range(N):
    for j in range(M):
        # 현재 위치에서 BFS 수행
        if bfs(i, j) == True:
            count += 1

print(count)

end_time = time.time()
print("time : ",end_time - start_time)
# for col in range(N):
#     for row in range(M):
#         pass
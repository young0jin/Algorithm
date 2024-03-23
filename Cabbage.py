# 백준 1012 

# 1 : 배추가 심어져 있는 땅
# 0 : 배추가 심어져 있지 않은 땅
# 배추가 심어져 있는 땅으로 이동 가능
# 이동 : 상하좌우

# output 몇 마리의 지렁이가 필요한지

from collections import deque

def bfs(i, j, M, N):
    directions = [(0,1) , (0,-1), (1,0), (-1,0)]
    queue = deque([(i, j)])

    matrix[i][j] = 0
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))

 

T = int(input())
for _ in range(T):
    M, N, K= map(int, input().split())

    matrix = [[0 for _ in range(N)] for _ in range(M)]
    worm = 0

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for i in range(M):
        for j  in range(N):
            if matrix[i][j] == 1:
                worm += 1
                bfs(i, j, M, N)
    print(worm)     


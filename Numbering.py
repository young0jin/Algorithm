# 백준 2667

# 첫 번째 줄 지도의 크기 N개
# N개의 자료

# 출력 : 붙어있는 1의 덩어리 수
from collections import deque

def bfs(i, j, N):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque([(i,j)])
    
    num = 1
    matrix[i][j] = '0'

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == '1':
                matrix[nx][ny] = '0'
                queue.append((nx, ny))
                num +=1 
    
    return num


N = int(input())
matrix = [] * N
output = []

for _ in range(N):
    matrix.append(list(input().strip()))


for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1': 
            output.append(bfs(i, j, N))

output.sort()
print(len(output))
for item in output: print(item)
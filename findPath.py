#백준 2178

#n * m 배열 
#1 : 이동 0: 이동못함

import sys
from collections import deque

n, m = map(int, input().split())

arr = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    arr.append(list(input()))


queue = deque([(0, 0, 1)])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited[0][0] = True

while queue:
    x, y, move = queue.popleft()

    if x == n-1 and y == m-1: 
        print(move)
        break
    
    for dx, dy in directions:
        nx = dx + x
        ny = dy + y

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == '1':
            visited[nx][ny] = True
            queue.append((nx, ny, move + 1))
        
    


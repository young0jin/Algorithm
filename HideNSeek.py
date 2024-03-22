#백준 1697
#숨바꼭질

# n : 술래 위치
# k : 숨어있는 사람 위치
# 1초 : 현위치로 X +1 or X -1 or 2*X
from collections import deque

def bfs(n, k):
    visited = [0 for _ in range(100001)]
    queue = deque([n])
    while queue:
        x = queue.popleft()
        
        if x == k: 
            return visited[x]
            

        for i in (x + 1, x - 1, 2 * x):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)



n, k = map(int, input().split())
print(bfs(n, k))

    
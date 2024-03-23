#백준 1260
#그래프를 DFS로 탐색한 결과 출력
#그래프를 BFS로 탐색한 결과 출력

#첫째줄 정정의 갯수 N, 간선의 갯수 M, 탐색을 시작할 정점의 번호 V
#M개의 줄 : 간선이 연결하는 두 정점의 번호
#(단, 두 정점 사이에 여러 개의 간선이 존재할 수 있음)

#output : 첫번재 줄 (DFS 수행 결과) 두번째줄 (BFS 수행 결과)
#V부터 방문된 점을 순서대로 출력

import sys
from collections import deque
sys.setrecursionlimit(10**6)

def searchBFS(graph, u, visited, n):
    queue = [u]
    visited[u] = True
    
    while queue:
        u = queue.pop(0)
        print(u, end = ' ')
        for i in range(1, n+1):
            if not visited[i] and graph[u][i] == 1:
                visited[i] = True
                queue.append(i)
                
        
        

def searchDFS(graph, u, visited, n):
    visited[u] = True
    print(u, end = ' ')
    for i in range(1, n+1):
        if graph[u][i] == 1 and not visited[i]:
            searchDFS(graph, i, visited, n)


n, m, v = map(int, sys.stdin.readline().split())

bfsVisited = [False] * (n+1)
dfsVistied = bfsVisited.copy()
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    graph[u][w] = graph[w][u] = 1

searchDFS(graph, v, dfsVistied, n)
print()
searchBFS(graph, v, bfsVisited, n)






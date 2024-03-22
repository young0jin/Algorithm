#백준 1260
#그래프를 DFS로 탐색한 결과 출력
#그래프를 BFS로 탐색한 결과 출력

#첫째줄 정정의 갯수 N, 간선의 갯수 M, 탐색을 시작할 정점의 번호 V
#M개의 줄 : 간선이 연결하는 두 정점의 번호
#(단, 두 정점 사이에 여러 개의 간선이 존재할 수 있음)

#output : 첫번재 줄 (DFS 수행 결과) 두번째줄 (BFS 수행 결과)
#V부터 방문된 점을 순서대로 출력

import sys

def searchBFS()
def searchDFS()

n, m, v = map(int, sys.stdin.readline().split())

bfsVisited = [False] * (n+1)
dfsVistied = [False] * (n+1)

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    u, w = map(int, sys.stdin.readline().split())
    graph[u][w] = graph[w][u] = 1

def searchDFS(dfsVisited, v)



# 백준 11724

# 방향 없는 그래프, 연결 요소 개수를 구하는 프로그램
# N, M ( N : 정점의 갯수 M : 간선의 개수)
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(graph, v, visited):
    if not visited[v]: visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)


N, M = map(int, sys.stdin.readline().split())
visited = [False] * (N+1)
graph = defaultdict(list)
component = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        component += 1
        dfs(graph, i, visited)

print(component)

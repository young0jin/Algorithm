# 원점 (0,0) to (0, n+1)
# 수평 선분
from collections import defaultdict

n = int(input())
dp = defaultdict(lambda: defaultdict(lambda: float("inf")))
obstacles = []
dp[0][0] = 0

for _ in range(n):
   x, y = map(int, input().split())
   obstacles.append((x, y))

for i in range(1, n + 1):
   l_i, r_i = obstacles[i-1]
   
   for x in dp[i - 1].keys():
      if x < l_i:
         dp[i][l_i] = min
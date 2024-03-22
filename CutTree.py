# 줄지어 있는 나무의 갯수 n
# 필요한 나무의 길이 M
# 절단기의 높이 H

# 원하는것? m을 구하기 위해 지정해야 하는 최대 절단기 높이 h
import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(sys.stdin.readline()).sort()

low, high = 1, max(trees)
h = high
while low <= high:
    mid = (low + high) // 2
    temp = 0
    for tree in trees:
        if tree - h > 0 : temp += (tree- h)
        
    if temp < m:
        
        

print(h)
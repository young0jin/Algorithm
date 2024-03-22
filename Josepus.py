# N명의 사람이 원으로 앉아 있음
# 양의 정수 K
# K번째 사람 제거
# 다 제거될 때 까지 진행
import sys
from collections import deque
#n : 인원 수 k : 제거 숫자

n, k = map(int, sys.stdin.readline().split())

people = deque()
result = []

for i in range(1, n+1):
    people.append(i)

while people:
    for i in range(k - 1):
        people.append(people.popleft())
            
    result.append(people.popleft())
    
print( "<" + ", ".join(map(str, result)) + ">" )

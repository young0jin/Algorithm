# 첫번째줄 테스트케이스 숫자
# (문서의 개수), (출력 순서가 궁금한 문서의 현 QUEUE 순서))\
# 두번째줄 N개의 문서의 중요도 (1~9) (완)

import sys
from collections import deque

t = int(sys.stdin.readline())
out = ""
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    priority = deque(map(int, sys.stdin.readline().split()))

    output = 0
    while priority:
        highValue = max(priority)
        
        value = priority.popleft()
        m -= 1
        
        if value < highValue:
            priority.append(value)
            if m < 0:
                m = len(priority) - 1
        else:
            output += 1
            if m < 0:
                out += str(output) + "\n"
                break

print(out.rstrip("\n"))
    

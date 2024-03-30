#백준 1931

# N개의 회의실
# N줄 각 회의 시작 시간 끝나는 시간

import sys

N = int(input())
times = []
answer = 0 # 진행 가능한 회의 갯수 
tot = 0 #진행 시간

# s : start e : end
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    times.append((s,e))

times.sort(key = lambda x : (x[1], x[0]))


for time in times:
    if tot <= time[0]:
        tot = time[1]
        answer += 1
print(answer)
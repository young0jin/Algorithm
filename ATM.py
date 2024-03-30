# 백준 11399

# 첫번째 줄: N명 사람 대기 (1~N)
# 두번째 줄: P_i  : 인출 시 걸리는 시간

N = int(input())
P = list(map(int, input().split()))
P.sort()

for i in range(1, N):
    P[i] += P[i-1]

print(sum(P))

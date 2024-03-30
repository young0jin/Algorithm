#백준 2875
# n : 참가 여학생 수
# m : 참가 남학생 수
# K : 인턴 참가 명수

# 팀 결성 : 2명의 여학생 1명의 남학생
# 많은 팀을 만드는 것이 목적

n , m, k = map(int, input().split())
output = 0

while n >= 2 and m >= 1 and (n - 2) + (m - 1) >= k:
    n -= 2
    m -= 1
    output += 1

print(output)
# 백준 10610

# 30의 배수가 되는 가장 큰 수 만들기
# 3의 배수 특징은 : 각 자리의 합이 3의 배수일 경우
# 4의 배수 특징: 끝 2자릿수가 4의 배수인 경우
# 6의 배수 특징 : 3의 배수 중 짝수
# 9의 배수 : 각 자리의 합의 9의 배수

import sys

N = input()
N = [int(char) for char in N]

if 0 not in N: output = -1
else:
    N.sort(reverse = True)
    if sum(N) % 3 == 0:
        output = int(''.join(map(str, N)))
    else: output = -1

print(output)
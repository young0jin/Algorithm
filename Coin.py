# 백준 11047
# 동전 N종류
# 가치의 합 K
# 필요한 동전의 개수 최소값 구하기

N, K = map(int, input().split())
coins = []
count = 0
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse = True)

for coin in coins:
    if K >= coin:
        temp = K // coin
        count += temp
        K = K - coin * (temp)

print(count) 
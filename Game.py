#백준 12845
# n  : 카드 수
# L : 카드 레벨

n = int(input())
gold = 0
L = list(map(int, input().split()))

L.sort(reverse = True)

for i in range(1, n):
    gold += L[0] + L[i]

print(gold)
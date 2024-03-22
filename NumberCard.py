#n개의 카드
#m : 정수
# 첫째줄: 상근이가 갖고 있는 카드 갯수
# 둘째줄: 상근이가 갖고 있는 카드 종류
# 셋째줄: 알고 싶은 카드의 갯수
# 넷째줄: 알고 싶은 카드의 종류

import sys
from collections import Counter

getCard = int(sys.stdin.readline())
getCardList = list(map(int, sys.stdin.readline().split()))
knowCard = int(sys.stdin.readline())
knowCardList = list(map(int, sys.stdin.readline().split()))
output = []

cardFrequency = dict(Counter(getCardList))

for num in knowCardList:
    output.append(cardFrequency.get(num, 0))

print(' '.join(str(x) for x in output))
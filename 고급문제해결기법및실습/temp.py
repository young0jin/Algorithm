from collections import defaultdict
n, k = map(int, input().split())
p = list(map(int, input().split()))

count = {p[0]:1}
answer = n + 1
left = 0
right = 0
flag = False 
dd = defaultdict(list)

while(left < len(p) and right < len(p)):
    if len(count) == k:
        answer = min(answer, right - left + 1)
        
        if answer == right - left +1:
            dd[answer].append((left, right))

        count[p[left]] -= 1
        if count[p[left]] == 0:
            del count[p[left]]                  
        left += 1

    else:
        right += 1 
        if right == len(p):
            break
        count[p[right]] = count.get(p[right], 0) + 1


if answer > len(p) or answer not in dd.keys():
    answer = 0
else:
    valid = False
    for left, right in dd.get(answer, []):
        color = set(p[right +1 : ] + p[0:left])
        if len(color) == k : 
            valid = True
            break
    if not valid : answer = 0
print(answer)
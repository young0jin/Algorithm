#무지개 찾기
n, k = map(int, input().split())
p = list(map(int, input().split()))

count = {p[0]:1}
answer = n + 1
left = 0
right = 0
while(left < len(p) and right < len(p)):
    if len(count) == k:
        answer = min(answer, right - left + 1)
            
        count[p[left]] -= 1
        if count[p[left]] == 0:
            del count[p[left]]                  
        left += 1

    else:
        right += 1 
        if right == len(p):
            break
        count[p[right]] = count.get(p[right], 0) + 1
        # if p[right] in count.keys():            
        #     count[p[right]] += 1
        # else:
        #     count[p[right]] = 1

print(left-1, right-1)
answer = 0 if answer > len(p) else answer
print(answer)

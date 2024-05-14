from collections import defaultdict
n, k = map(int, input().split())
p = list(map(int, input().split()))

count = {p[0]:1}
answer = n + 1
left = 0
right = 0
flag = False 
dd = defaultdict(bool)

def check_p(t_left, t_right):
    t_flag = False
    color = set(p[t_right +1 : ] + p[0:t_left])

    if len(color) == k: t_flag = True
    return t_flag

while(left < len(p) and right < len(p)):
    if len(count) == k:
        answer = min(answer, right - left + 1)
        
        if answer == right - left +1:
            flag = check_p(left, right)
            if flag == True : dd[answer] = flag

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
    
print(answer)
# n명의 대기자 times
# 각 심사관에 걸리느 시간
# 심사를 받는데 걸리는 시간을 최소
# 최소 시간 

def solution(n, times):
    start = 1
    end = max(times) * n
    answer = end
    
    while start <= end: 
        mid = (start + end) // 2
        temp = 0
        
        for time in times:
            temp += (mid // time)
        
        if temp >= n:
            answer = min(mid, answer)
            end = mid -1
        else:
            start = mid + 1
            
    
    return answer
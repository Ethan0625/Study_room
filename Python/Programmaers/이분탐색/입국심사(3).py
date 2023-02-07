def solution(n, times):
    '''
    7 14 21
    10 20 30
    최소지점을 찾는 것
    '''
    if n==1:
        answer = min(times)
    start, end = min(times), max(times)*(n//len(times))
    res = end
    while start <= end:
        mid = (start + end) // 2
        
        people = 0
        for time in times:
            people += (mid // time)
            
        if people < n:
            start = mid+1
        else: #people >= n:
            end = mid-1
            res = min(res, mid)
            
    return res
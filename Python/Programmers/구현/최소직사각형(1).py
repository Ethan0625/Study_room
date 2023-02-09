def solution(sizes):
    w = [max(v) for v in sizes]
    h = [min(v) for v in sizes]
    answer = max(w)*max(h)
    
    return answer
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(1,len(citations)+1):
        tmp = citations[i-1]
        if i>tmp:
            return i-1
        elif i==tmp:
            return i
    return len(citations)
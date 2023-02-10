# 이전 풀이
from collections import deque
def solution(numbers, target):
    '''
    다음으로 넘어가는 조건
    해당 인덱스까지 계산결과 이후 전부 더하거나 뺐을 때 해당 값보다 크거나 작으면 continue
    continue는 다음 인덱스로 넘어가는 것
    '''
    n = len(numbers)
    idx = 0
    answer=0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-numbers[0],0])
    while queue:
        tmp ,idx = queue.popleft()
        idx+=1
        if idx<n:
            queue.append([tmp+numbers[idx],idx])
            queue.append([tmp-numbers[idx],idx])
        else:
            if tmp==target:
                answer+=1
    
    return answer

#변경 풀이
def solution(numbers, target):
    '''
    0부터 시작 +1 -1을 한 결과를 전부 group안에 넣어둠
    bfs에 가까움
    전체 과정을 추적함
    '''
    group = [[0]]
    
    
    for j in range(len(numbers)):
        answer = group.pop()
        tmp = []
        for k in answer:
            tmp.append(k+numbers[j])
            tmp.append(k-numbers[j])
        group.append(tmp)
    
    answer = group[-1].count(target)
    return answer
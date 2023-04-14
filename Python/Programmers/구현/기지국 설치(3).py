from collections import deque
import math
def solution(n, stations, w):
    # 1-2, 6-9
    # 2, 4
    # W = 1+2*(w)
    # 2-w
    answer = 0
    W = 2*w+1
    dist = []
    # 사이값들만 넣기
    for i in range(1, len(stations)):
        dist.append((stations[i]-w-1)-(stations[i-1]+w))
        
    # 앞, 뒤 값 넣기
    dist.append(stations[0]-w-1)
    dist.append(n-(stations[-1]+w))

    # answer 정리
    for i in dist:
        if i<=0:
            continue
        else:
            answer+=math.ceil(i/W)
    return answer
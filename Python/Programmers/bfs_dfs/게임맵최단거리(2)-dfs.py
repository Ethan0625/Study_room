from collections import deque
def solution(maps):
    '''
    상하좌우 움직임
    y = [-1,1,0,0]
    x = [0,0,-1,1]
    왔던길을 다시가지는 않아야함
    양갈래길을 가는 경우, 1인경우 + 0와 1이 아닌경우 최소값
    '''
    answer = 0
    y_dir = [-1,1,0,0]
    x_dir = [0,0,-1,1]
    y_max = len(maps)
    x_max = len(maps[0])
    
    que = deque()
    que.append([0,0,1])

    while que:
        dy, dx, v = que.popleft()
        for i in range(len(y_dir)):
            ny = dy+y_dir[i]
            nx = dx+x_dir[i]
            # 기존 1값이 있는 부분만 찾기위해 리스트를 만들고 해당 리스트에서 찾는 과정이 있었음
            # 해당 과정으로 인해 시간이 더 걸려 아래와 같이 조건식으로 변경함
            # 이로 인해 효율성 개선
            if nx>=0 and nx<x_max and ny>=0 and ny<y_max:
                if maps[ny][nx]==1:
                    maps[ny][nx] = v+1
                    que.append([ny,nx,v+1])
    answer = maps[-1][-1]
    print(answer)
    if answer == 1 or answer==0:
        return -1
    else:
        return answer
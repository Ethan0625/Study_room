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
    s_y = 0
    s_x = 0
    val_loc = [[i,j] for i in range(len(maps)) for j in range(len(maps[i])) if maps[i][j]==1]
    
    que = deque()
    que.append([s_y,s_x])

    
    while que:
        v = que.popleft()
        for i in range(len(y_dir)):
            if [v[0]+y_dir[i], v[1]+x_dir[i]] in val_loc:
                if maps[v[0]+y_dir[i]][v[1]+x_dir[i]]==1:
                    maps[v[0]+y_dir[i]][v[1]+x_dir[i]] = maps[v[0]][v[1]]+1
                    que.append([v[0]+y_dir[i],v[1]+x_dir[i]])
    answer = maps[-1][-1]
    if answer == 1 or answer==0:
        return -1
    else:
        return answer
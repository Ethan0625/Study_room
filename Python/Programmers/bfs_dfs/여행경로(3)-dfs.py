import collections
# 푸는 중
def solution(tickets):
    tict = collections.defaultdict()
    # 1. ticket을 {start:[end1, end2]}의 형태로 만들어줌(그래프화)
    for i in tickets:
        tict[i[0]] = []
        
    for j in tickets:
        tict[j[0]].append(j[1])
        tict[j[0]].sort(reverse=True)
    
    # 지나왔던 길 확인을 위한 tmp_list(passed)
    tmp_list = ['ICN']
    answer = []
    while tmp_list:
        # key는 지나왔던 길의 마지막
        # 해당 key를 기준으로 다음 목적지를 정하기 때문
        key = tmp_list[-1]
        # key가 없으면서 해당 key의 값이 0이라면
        if key not in tict.keys() or len(tict[key])==0:
            # 해당 key로는 다음 목적지가 없으므로, 해당되는 key를 빼 answer(dest)에 넣어 놓는다.
            # end1, end2가 있는 경우에 end2의 값에 해당되는 목적지가 없기 때문에 end1을 우선적으로 가야하고
            # end1을 통해 다른 곳을 가더라도, tmp_list에 우선적으로 들어가게 됨
            # 따라서, 모든 곳을 지나갔을 때, tmp_list에서 역순으로 하나씩 빼서
            # answer에 넣어주면 모든 목적지를 지나온 것이 되고
            # ICN부터 순차적으로 가기 위해서는 역순으로 돌려주어야 함.
            last_dest = tmp_list.pop()
            answer.append(last_dest)
        else:
            dest = tict[key].pop()
            tmp_list.append(dest)
    return answer[::-1]

# 비슷한 개념 활용한 풀이
def solution(tickets):
    # 1. 그래프 생성
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]  

    # 2. 시작점 - [끝점] 역순으로 정렬    
    for r in routes.keys():
        routes[r].sort(reverse=True)

    # 3. DFS 알고리즘으로 path를 만들어줌.
    st = ["ICN"]
    path = []
    
    while st:
        top = st[-1]

        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    
    # 4. 만든 path를 거꾸로 돌림.
    answer = path[::-1]
    return answer
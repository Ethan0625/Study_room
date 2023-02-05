'''
- 그리디 알고리즘
    - 크루스칼 알고리즘 활용
        - 크루스칼은 최소신장 거리를 구할 때 사용하는 알고리즘
        - 섬을 연결하는데 소요되는 비용을 작은순서대로 차례로 나열(heapq.heappush(넣을 곳, 값)
        - 이미 연결되어있는지 확인할 테이블 필요
            - 파이썬의 경우 set을 활용하면 됨
            - 연결 된 값을 set.update(번호1,번호2)로 넣게 되면 자동으로 중복 제거되어 들어가게 됨
        - while 문을 돌면서 정리된 데이터를 확인하고 섬의 번호가 테이블에 있는지 확인
            - 확인할 섬 번호 두개가 전부 들어가 있다면 이미 연결되어있으므로 패스
            - 아니라면 둘 중의 하나가 테이블에 들어가있는 경우에만 테이블을 업데이트 해주고 해당 cost를 answer에 더해준다.
    - 원래의 크루스칼 알고리즘은 연결된 테이블을 새로 만들고 해당 테이블을 직접 업데이트 하는 방법으로 find_parent와 union_parent를 따로 구현하여 사용한다.
    - 하지만 해당 문제는 그럴 필요가 없음 or 원래 이렇게 구현해도 상관 없을지도
'''

import heapq

def get_parent(c,node):
    if c[node]==node:
        return node
    return get_parent(c,c[node])

# 두 원소가 속한 집합을 합치기
def union_parent(parent, edge):
    a = get_parent(parent, edge[1])
    b = get_parent(parent, edge[2])
    if not a==b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
        return edge[0]
    return 0


def solution(n, costs):
    answer = 0
    parent = [x for x in range(n)]

    edge = [(cost, node1, node2) for node1,node2,cost in costs]
    heapq.heapify(edge)
    
    while edge:
        answer += union_parent(parent, heapq.heappop(edge))
    
    return answer
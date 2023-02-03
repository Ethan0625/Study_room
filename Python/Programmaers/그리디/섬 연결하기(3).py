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
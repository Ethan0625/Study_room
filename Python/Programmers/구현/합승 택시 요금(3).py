def solution(n, s, a, b, fares):
    # 최저 거리 산정
    # 합승이 포인트
    # A와 B 각각 가는 길을 확인 answer = 합승 비용(0) + 각각 비용(A+B)
    # 지점별로 합승해서 간다고 했을 때 각 지점별로 나눠서 가는 것을 찾아야함
    # 즉, 한 지점에서 각자의 집으로 가는 길을 확인
    # 각각 가는 로직 활용
    # answer = min(합승 비용 + 각각 비용)
    max_v = 0
    
    for i in fares:
        max_v+=i[2]
    cost = [[max_v]*(n+1) for _ in range(n+1)]
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if j==k:
                    cost[j][k]=0
                else:
                    cost[j][k]=min(cost[j][i]+cost[i][k],cost[j][k])
    answer = max_v
    for i in range(1,n+1):
        answer = min(cost[s][i]+cost[i][a]+cost[i][b],answer)
    return answer
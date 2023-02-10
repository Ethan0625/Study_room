import collections
# 푸는 중
def solution(tickets):
    tict = collections.defaultdict()
    for i in tickets:
        tict[i[0]] = []
    for j in tickets:
        tict[j[0]].append(j[1])
        tict[j[0]].sort(reverse=True)
    tmp_list = ['ICN']
    answer = ['ICN']
    while tmp_list:
        key = tmp_list.pop()
        if key in tict.keys():
            if tict[key]!=[]:
                dest = tict[key].pop()
                answer.append(dest)
                tmp_list.append(dest)
    return answer
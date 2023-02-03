# from collections import deque
import heapq
def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time

    while h:
        print('idx :',k%food_num)
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        # 즉 최소시간 기준으로 전체를 돌았을 때의 시간이 됨
        t = (h[0][0] - previous) * food_num
        print('eat_time :',t)
        print('k :',k)
        print('previous :', previous)
        print('h :',h)
        print('------')
        
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break
    print('final idx :',idx)
    print('final h :',h)
    print('answer :',answer)
    return answer
            
    # while k:
    #     temp=dq.heappop()
    #     print(temp)
    #     k-=1
    #     if temp[1]<k:
    #         k-=temp[1]
    #         if temp[1]!=0:
    #             dq.append(temp)
    #         k-=1
    # return dq[0][0]
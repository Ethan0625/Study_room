'''
- 해당 문제는 기존에 파이썬 내장 라이브러리인 collections의 deque를 활용하여 풀었다.
- 하지만 deque 를 활용할 경우, 넣어서 먹는데 소요되는 시간을 빼고 다시 넣는 과정을 반복하면서 효율성이 박살이 난다.
- 이를 보안하고자 구글링을 진행하였고, 구글링에서 heapq(최소힙)을 활용한 방법이 있다는걸 확인하였다.
- heqpq를 활용한 방법
    - food_times 리스트를 [(소요시간,idx+1)]로 다시 정리한다.
    - food_times 리스트를 heapq.heapify(리스트)를 활용하여 소요시간 기준으로 정리한다.
    - food_times가 없어질 때까지 다음의 과정을 반복한다.
        - 이전에 소요된 시간의 초기값은 0이다.
        - food_times의 첫번째 먹방 소요시간에서 기존에 소요된 시간을 빼주고 여기에 남은 음식의 개수를 곱해준다.
        - 해당 시간이 주어진 기준시간 k보다 크거나 같다면 아래의 과정을 거친다.
            - k에서 해당 시간을 빼준다.
            - food_times에서 heappop을 진행하여, 빠져나온 값의 먹방 소요시간을 previos로 지정해준다.
            - 남은 음식의 개수를 -1해준다.
        - 해당 시간이 주어진 기준시간 k보다 작다면 아래의 과정을 거친다.
            - k를 남은 음식 개수로 나눈 나머지 값을 index기준 값으로 잡는다.
            - food_times는 현재 cost가 작은 순서대로 정렬되어있으므로, 이를 index 기준으로 변환해준다.
            - 위에서 기존 idx+1을 해준 이유는 k시간 이후에 확인할 답이 마지막으로 먹었던 음식이 아닌, 다음에 먹을 음식이기 때문이다.
            - 변환 이후, food_times[idx][1]을 리턴해준다
'''
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
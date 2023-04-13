## DFS/BFS
### 관련 알고리즘
- 스택 (Stack)
    - 먼저 들어 온 데이터가 나중에 나가는 형식 (선입후출 - FILO)
    - 파이썬으로 구현 할 경우, 리스트를 활용하여 구현할 수 있으며 단순 pop()을 사용하면 됨
- 큐 (Queue)
    - 먼저 들어온 데이터가 먼저 나가는 형식 (선입선출 - FIFO)
    - 파이썬으로 구현 할 경우, collections 라이브러리의 deque를 활용하여 구현할 수 있으며 popleft()를 사용함
- 재귀 (Recursive)
    - 자기 자신을 다시 호출하는 함수
    - 반복문으로 구현 된 코드는 재귀 함수로 구현 할 수 있음

### 관련 알고리즘 예제
- 유클리드 호제법
    - 두 자연수 A, B에 대해서 A가 B보다 클 때, A를 B로 나눈 나머지를 R이라 한다.
    - 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
    ```python
    def recursive(a,b):
        if a%b==0:
            return b
        else:
            return recursive(b,a%b)
    ```
---
## DFS(Depth-First Search)
### 개념  
- **그래프**에서 값을 탐색할 때, 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조(혹은 재귀 함수)를 이용하여 구현되며, 구체적인 동작 과정은 다음과 같다.  

``` 
(1) 탐색 시작 노드를 스택에 삽입하고 방문 처리한다. 

(2-1) 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면, 그 노드를 스택에 넣고 방문 처리한다.

(2-2) 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.

(3) 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
```

### 중요점  
- 꼭 스택만 가지고 구현할 필요는 없다.
- 2번의 과정을 정의해야한다.
- 재귀함수가 쓰일 수 있는 이유는 3번의 반복덕분이다.

### 예시
- 예시문제 : <img src ="https://school.programmers.co.kr/assets/bi-symbol-light-49a242793b7a8b540cfc3489b918e3bb2a6724f1641572c14c575265d7aeea38.png" width="10" /> [프로그래머스 여행경로-level3](https://school.programmers.co.kr/learn/courses/30/lessons/43164)
    ```
    문제 설명
    주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

    항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

    제한사항
    1. 모든 공항은 알파벳 대문자 3글자로 이루어집니다.  
    2. 주어진 공항 수는 3개 이상 10,000개 이하입니다.  
    3. tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.  
    4. 주어진 항공권은 모두 사용해야 합니다.  
    5. 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.  
    6. 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
    ```

### 내 풀이

```python
import collections
def solution(tickets):
    tict = collections.defaultdict()
    for i in tickets:
        tict[i[0]] = []
    for j in tickets:
        tict[j[0]].append(j[1])
        tict[j[0]].sort(reverse=True)
    # (1) 탐색 시작 노드를 스택에 삽입하고 방문 처리한다. 
    passed = ['ICN']
    answer = []
    # (3) 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
    while passed:
        key = passed[-1]
        if key not in tict.keys() or len(tict[key])==0:
            #(2-2) 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
            last_dest = passed.pop()
            answer.append(last_dest)
        else:
            # (2-1) 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면, 그 노드를 스택에 넣고 방문 처리한다.
            dest = tict[key].pop()
            passed.append(dest)
            
                
    return answer[::-1]
```
---
## BFS (Breath-First Search)
### 개념
- **그래프**에서 값을 탐색할 때, 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 이용하여 구현되며, 구체적인 동작 과정은 다음과 같다.  

``` 
(1) 탐색 시작 노드를 큐에 삽입하고 방문 처리한다. 

(2) 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다.

(3) 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
```

### 중요점
- 작성중

### 예시
- 예시문제 : <img src ="https://school.programmers.co.kr/assets/bi-symbol-light-49a242793b7a8b540cfc3489b918e3bb2a6724f1641572c14c575265d7aeea38.png" width="10" /> [프로그래머스 타겟넘버-level2](https://school.programmers.co.kr/learn/courses/30/lessons/43165)
    ``` 
    타겟 넘버
    문제 설명
    n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

    -1+1+1+1+1 = 3
    +1-1+1+1+1 = 3
    +1+1-1+1+1 = 3
    +1+1+1-1+1 = 3
    +1+1+1+1-1 = 3
    사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

    제한사항
    주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
    각 숫자는 1 이상 50 이하인 자연수입니다.
    타겟 넘버는 1 이상 1000 이하인 자연수입니다.
    ``` 
### 내풀이
```python
def solution(numbers, target):
    '''
    0부터 시작 +1 -1을 한 결과를 전부 group안에 넣어둠
    bfs에 가까움
    전체 과정을 추적함
    '''
    group = [[0]]
    
    
    for j in range(len(numbers)):
        answer = group.pop()
        tmp = []
        for k in answer:
            tmp.append(k+numbers[j])
            tmp.append(k-numbers[j])
        group.append(tmp)
    
    answer = group[-1].count(target)
    return answer
```

- 예시문제 : <img src ="https://school.programmers.co.kr/assets/bi-symbol-light-49a242793b7a8b540cfc3489b918e3bb2a6724f1641572c14c575265d7aeea38.png" width="10" /> [프로그래머스 등산코스 정하기-level3](https://school.programmers.co.kr/learn/courses/30/lessons/118669)
    ``` 
    문제 설명
    XX산은 n개의 지점으로 이루어져 있습니다. 
    각 지점은 1부터 n까지 번호가 붙어있으며, 출입구, 쉼터, 혹은 산봉우리입니다. 
    각 지점은 양방향 통행이 가능한 등산로로 연결되어 있으며, 
    서로 다른 지점을 이동할 때 이 등산로를 이용해야 합니다. 
    이때, 등산로별로 이동하는데 일정 시간이 소요됩니다.

    등산코스는 방문할 지점 번호들을 순서대로 나열하여 표현할 수 있습니다.
    예를 들어 1-2-3-2-1 으로 표현하는 등산코스는 1번지점에서 출발하여 
    2번, 3번, 2번, 1번 지점을 순서대로 방문한다는 뜻입니다.
    등산코스를 따라 이동하는 중 쉼터 혹은 산봉우리를 방문할 때마다 
    휴식을 취할 수 있으며, 휴식 없이 이동해야 하는 시간 중 
    가장 긴 시간을 해당 등산코스의 intensity라고 부르기로 합니다.

    당신은 XX산의 출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 다시 원래의 출입구로 돌아오는 등산코스를 정하려고 합니다. 다시 말해, 등산코스에서 출입구는 처음과 끝에 한 번씩, 산봉우리는 한 번만 포함되어야 합니다.
    당신은 이러한 규칙을 지키면서 intensity가 최소가 되도록 등산코스를 정하려고 합니다.
    ```

    ### 참조 풀이
    - 풀이에 실패하여 다른사람의 풀이를 참조하여 풀었음
    - 해당 문제는 다익스트라를 활용하여 풀이하여야 함.
    ```python
    import heapq
    from math import inf
    def solution(n, paths, gates, summits):
        # 경로를 찾는 문제
        # g->s->g로 돌아올 때 드는 costs 중 max값이 intensity
        # floyd_warshall을 활용해본다.
        
        # 간선 정리 (양방향)
        graph = [[] for _ in range(n + 1)]
        for i, j, w in paths:
            graph[i].append([j, w])
            graph[j].append([i, w])

        # 산봉우리 판별
        is_summit = [False] * (n + 1)
        for summit in summits:
            is_summit[summit] = True

        # gates 모두 시작 위치
        distance = [inf] * (n + 1)
        queue = []
        for gate in gates:
            distance[gate] = 0
            heapq.heappush(queue, [0, gate])

        # 다익스트라
        while queue:
            d, i = heapq.heappop(queue)
            # 산봉우리면 바로 continue
            # 이렇게 해야 두 개 이상의 산봉우리를 방문하지 않는다.
            if distance[i] < d or is_summit[i]:
                continue
            for j, dd in graph[i]:
                dd = max(distance[i], dd)
                if distance[j] > dd:
                    distance[j] = dd
                    heapq.heappush(queue, [dd, j])

        # 결과
        # 거리가 같으면 산봉우리의 번호가 작은 것을 출력해야 하므로
        # 산봉우리를 정렬하여 살펴보자.
        result = [-1, inf]

        for summit in sorted(summits):
            if distance[summit] < result[1]:
                result[0] = summit
                result[1] = distance[summit]
        return result
    ```
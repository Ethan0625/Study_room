## 정렬 알고리즘
### 정의
- 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용 됨

### 관련 알고리즘
1. 선택 정렬
	- 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞의 데이터와 바꾸는 것을 반복
    - 이중 for문으로 구현 가능
    - 예시
        ``` python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

        for i in range(len(array)):
            min_index = i # 가장 작은 원소의 인덱스
            # 가장 작은 원소인 이유는 
            # 가장 작은 원소를 맨 앞으로 스왑하기 때문
            for j in range(i+1,len(array)):
                if array[min_index] > array[j]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i] # swap
        ```  
    - 시간 복잡도 O(N<sup>2</sup>)
---
2. 삽입 정렬
    - 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 것
    - 선택 정렬에 비해 구현 난이도가 높지만 선택 정렬에 비해 속도가 좀 더 빠름
    - 예시
        ``` python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

        for i in range(1,len(array)):
            for j in range(i,0,-1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break
        ```  
    - 시간 복잡도 O(N<sup>2</sup>)
    - 단, 현재 리스트가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
---
3. 퀵정렬
    - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘
    - 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘
    - 병합 정렬과 저불어 대부분의 프로그래밍 언어의 정렬 라이브러리릐 근간
    - 기본적으로 첫 번째 데이터를 기준 데이터로 설정한다.
    - 기본예시
        ``` python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

        def quick_sort(array, start, end):
            if start >= end:
                return
            pivot = start
            left = start + 1
            right = end
            while(left <= right):
                while(left <= end and array[left] <= array[pivot]):
                    left +=1
                while(right > start and array[tight]>= array[pivot]):
                    right -=1
                if (left > right):
                    array[right], array[pivot] = array[pivot], array[right]
                else:
                    array[left], array[right] = array[right], array[left]
            quick_sort(array, start, right -1)
            quick_sort(array, right +1, end)
        
        quick_sort(array, 0, len(array)-1)
        ```  
    - 변환예시
        ``` python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

        def quick_sort(array):
            if len(array) <= 1:
                return array
            pivot = array[0]
            tail = array[1:]

            left_side = [x for x in tail if x <= pivot]
            right_side = [x for x in tail if x > pivot]
            
            return quick_sort(left_side) + [pivot] + quick_sort(right_side)
        ```  
    - 시간 복잡도 O(NlogN)
        - 최악의 경우 O(N<sup>2</sup>)
        - 이미 정렬 되어있는 경우가 최악
---
- 계수 정렬
    - 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
        - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
    - 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 O(N+K)를 보장한다.
     ``` python
        array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

        count = [0] * (max(array) + 1)

        for i in range(len(array)):
            count[array[i]] += 1
        
        for i in range(len(count)):
            for j in range(count[i]):
                print(i, enx=' ')
        ```  

### 예시 문제

```
- 동빈이는 두 개의 배열 A와 B를 가지고 있습니다. 
- 두 빼열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수 입니다.
- 동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다.
- 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 합니다.
- N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.
```

### 내 풀이

```python
def solution(N, K, A, B):
    A.sort()
    B.sort()
    A = A[K:]+B[-K:]
    return sum(A)
```
- 해당 경우는 A의 0부터 K번째 까지의 수가 B의 큰 수들보다 무조건 작을때만 알맞게 작동함
- 따라서 비교해주는 과정이 필요함

### 정답 풀이
```python
def solution(N, K, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(K):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break
    return sum(A)
```
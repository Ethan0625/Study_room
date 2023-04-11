## 그리디
### 포함되는 알고리즘
- 크루스칼 알고리즘
- 다익스트라

### 개념 

- 현재 상황에서 지금 당장 좋은 것만 고르는 알고리즘
- 문제를 풀기위한 최소한의 아이디어가 필요

### 중요점

- 그리디 알고리즘은 아이디어를 떠올리는 것도 중요하지만, 해당 아이디어가 정당한지를 검토하는 것도 중요

### 예시

```
n과 k로 정의되는 2개의 정수가 주어질때 아래와 같은 과정을 거쳐 1을 만들려고 한다.

1. n에서 1빼기
2. n을 k로 나누기

2의 경우는 n이 k로 나누어 떨어질 때만 가능하다.

1을 만드는데 최소한의 과정 횟수를 구하시오.
```

### 내 풀이

```python
def solution(n,k):
	answer = 0
	while n>1:
		if n%k==0:
			n = int(n//k)
			answer += 1
		else:
			n -= 1
			answer += 1
	return answer
```

이렇게도 풀리지만 한땀한땀 확인해야 하므로 수가 커지면 시간초과가 날 수 있음

```python
def solution(n,k):
	answer = 0
	while True:
		# 이렇게 target을 잡게 되면 n이 27인 경우 target은 25가 됨
		target = (n//k)*k
		# 결과에 나누어 떨어질 수 있을 때까지 빼는 횟수를 더해줌
		answer += (n-target)
		n = target
		if n<k:
			break
		result+=1
		n //= k
	
	# n이 k보다 작아졌으므로, 더이상 나눌 수 없음
	# 따라서 1이 될때까지 빼줘야 하므로 해당 횟수를 더해줌
	answer += (n-1)

	return answer
```

### 크루스칼 알고리즘
- 대표문제 : <img src ="https://school.programmers.co.kr/assets/bi-symbol-light-49a242793b7a8b540cfc3489b918e3bb2a6724f1641572c14c575265d7aeea38.png" width="10" /> [프로그래머스 섬 연결하기-level3](https://school.programmers.co.kr/learn/courses/30/lessons/42861)
- 개념 :  
	- 그래프 내의 모든 정점을 연결하는 최소 비용을 구하는데 사용 되는 알고리즘 (최소 신장 트리)
	- 여기서 신장 트리는 모든 노드를 연결하면서 사이클(노드가 전부 연결됨)이 일어나지 않은 트리를 말한다.
- 동작과정 :  
	- 간선 데이터를 비용에 따라 오름차순으로 정렬한다.(heapq나 sorted 활용) -> (cost, a, b)
	- 간선 데이터를 반복문으로 돌면서 아래의 과정을 반복한다.
		```
		1. a와 b의 부모노드를 확인한다.(연결되었는지 확인)
		2. 부모노드는 노드 번호의 크기가 작은것이 우선으로 정의된다.
		3. 부모노드가 다른경우, 부모노드를 업데이트 해주고 cost를 answer에 더해준다.
		4. 부모노드가 같은경우, 다음으로 넘어가 1번부터 3번까지의 과정을 반복한다.
		```
	- 간선데이터는 오름차순으로 정렬되어있으므로, 부모노드를 확인하며 업데이트를 해준다면 최소 신장 트리를 이루는 비용을 확인할 수 있다.
- 예시문제 풀이
	- heapq 활용 및 함수 활용 풀이
		``` python
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
		```
	- 함수 미구현 풀이
		``` python
		def solution(n, costs):
		# 크루스칼 알고리즘
		# 부모 노드를 찾아 해당 노드가 연결되는 edge를 찾아야함(함수화)
		# 전체가 다 연결 된 경우의 비용
		answer = 0
		costs.sort(key = lambda x: x[2]) 
		link = set([costs[0][0]])
		print(link)

		# Kruskal 알고리즘으로 최소 비용 구하기
		while len(link) != n:
			for v in costs:
				# set을 활용하여, 해당 node가 있는지 확인함으로써, 부모노드 업데이트를 간단하게 구현
				if v[0] in link and v[1] in link:
					continue
				if v[0] in link or v[1] in link:
					# set이므로, 중복된 데이터는 생략 됨
					link.update([v[0], v[1]])
					print(link)
					answer += v[2]
					break
					
		return answer
		```

- 포함되는 알고리즘
    - 크루스칼 알고리즘
    - 다익스트라

개념 

- 현재 상황에서 지금 당장 좋은 것만 고르는 알고리즘
- 문제를 풀기위한 최소한의 아이디어가 필요

중요점

- 그리디 알고리즘은 아이디어를 떠올리는 것도 중요하지만, 해당 아이디어가 정당한지를 검토하는 것도 중요

예시

n과 k로 정의되는 2개의 정수가 주어질때 아래와 같은 과정을 거쳐 1을 만들려고 한다.

1. n에서 1빼기
2. n을 k로 나누기

2의 경우는 n이 k로 나누어 떨어질 때만 가능하다.

1을 만드는데 최소한의 과정 횟수를 구하시오.

내 풀이

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
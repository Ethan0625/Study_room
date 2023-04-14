def solution(a):
    # 맨 왼쪽, 오른쪽은 그냥 남길 수 있음
    # 따라서 시작 최소값을 inf로 설정
    # 포인터가 양쪽으로 이동하면서 기존 최소값을 갱신하게 되면 그 값이 최소값이 되므로
    # 이전 최소값을 삭제하고(큰값 삭제) 남길 수 있음
    result = [False for _ in range(len(a))]
    minFront, minRear = float("inf"), float("inf")
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True

    return sum(result)
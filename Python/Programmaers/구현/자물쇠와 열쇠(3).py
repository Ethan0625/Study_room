def spin_right(arr):
    # 정사각 행렬(key)의 순서를 뒤에서 부터 역순으로 돌리고(zip(*key[::-1]))
    # 이를 풀어서 n*n의 array에서 n열의 데이터로 n길이의 n*n행렬을 다시 만듦(map)
    # map()에 list가 들어간 이유는 사실 list()가 내장함수이기 때문
    return list(map(list, zip(*arr[::-1])))

def check(arr, N):
    answer = True
    for ix in range(N):
        for iy in range(N):
            if arr[ix + N][iy + N] != 1:
                return False
    return answer

def solution(key, lock):
    '''
    키를 돌려봐야함(정상,90도,180도,270도)
    [0,0,0]
    [1,0,0]
    [0,1,1]
    
    [0,1,0]
    [1,0,0]
    [1,0,0]
    
    [1,1,0]
    [0,0,1]
    [0,0,0]
    
    [0,0,1]
    [0,0,1]
    [0,1,0]
    '''
    M = len(key)
    N = len(lock)
    # 3배 더 큰 자물쇠 생성
    new_lock = [[1] * N * 3 for _ in range(N * 3)]
    # 기존 자물쇠를 새로운 자물쇠 가운데에 위치
    for ix in range(N):
        for iy in range(N):
            new_lock[ix + N][iy + N] = lock[ix][iy]
    # 시계방향으로 4번 돌림
    for _ in range(4):
        key = spin_right(key)
        for lock_ix in range(N * 2):
            for lock_iy in range(N * 2):
                # key를 new_lock에 꽂음
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] += key[key_ix][key_iy]
                # new_lock의 중앙만 확인
                if check(new_lock, N):
                    return True
                # key를 new_lock에서 뺌
                for key_ix in range(M):
                    for key_iy in range(M):
                        new_lock[lock_ix + key_ix][lock_iy + key_iy] -= key[key_ix][key_iy]
    return False
def solution(name):
    '''
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 24 25 26
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10  9  8  7  6  5  4  3  2  1
    a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    현재 위치에서 앞으로 가는게 더 나은가 뒤로 가는게 더 나은가 최소를 찾아야함(min)
    i번째일 때, 그냥 쭉가는 경우(len(name)-1/첫번째부터 시작함),뒤로 돌아가는게 나은가
    결국 가장 긴 A를 기준으로 왼쪽에서 시작하느냐 오른쪽에서 시작하느냐임
    가장 긴 A를 어떻게 찾는가?
    "JABAAAAZ"
    '''
    # name = "BBBBAAAABA"
    answer = 0
    # print(name)
    min_move = len(name)-1
    for i,s in enumerate(name):
        cnt = ord(s)-65
        if cnt>13:
            cnt = cnt-((cnt-13)*2)
        answer += cnt
        
        # 다음 글자가 연속된 A인지 확인
        next = i + 1
        while next < len(name) and name[next] == 'A':
            # 연속되었다면 최대 연속 길이를 확인
            next += 1
        
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        # min_move : 
        # 기존 전체 길이
        
        # 2 *i + len(name) - next : 
        # 처음부터 시작해서 진행한 후 긴 A를 만나면 다시 돌아가 마지막으로 넘어가는 방식 따라서 2*i가 다시 돌아가는 형태가 됨. index이므로 처음은 0이 되고 남은 길이만큼 이동하는 걸로 생각하면 됨
        
        # i + 2 * (len(name) -next) :
        # 반대의 경우로 생각하는 것.
        # 바로 마지막으로 가서 처음방향으로 진행하다가, 다시 마지막에서 처음으로 넘어가 진행하는 것
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
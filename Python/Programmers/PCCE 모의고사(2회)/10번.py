'''
[PCCE 모의고사 2] 10번
문제 설명
머쓱이는 '생명 게임'이라고 알려진 프로그램을 만들려고 합니다. 생명 게임은 2차원 보드에서 이루어지며, 각각의 칸은 0이 저장된 죽은 칸이거나 1이 저장된 살아있는 칸입니다. 이때 자기 자신의 값과 주변 이웃한 칸들의 값에 따라 다음 세대에서 각 칸의 값이 정해집니다.

머쓱이가 만든 생명 게임의 규칙은 다음과 같습니다.

살아있는 칸 주변에 이웃이 2명 이하로 존재하면 그 칸은 다음 세대에 죽는다
살아있는 칸 주변에 이웃이 5명 이상 존재하면 그 칸은 다음 세대에 죽는다
죽어있는 칸 주변에 이웃이 정확히 2명 존재하면 그 칸은 다음 세대에 살아난다.
그 이외의 경우에는 살아있거나 죽은 상태가 유지된다.

검사 할 점의 개수n과 처음 보드의 상태 board, 점의 좌표를 나타내는 정수쌍 [a,b]가 n개 담긴 리스트 position이 주어졌을 때, 한세대 뒤에 board[a][b] 칸의 상태 리스트를 return하는 함수를 완성해주세요.
'''
def solution(n, board, position):
    answer = []
    y_max = len(board)
    x_max = len(board[0])
    print(y_max)
    print(x_max)
    y = [-1,1,0,0,-1,-1,1,1]
    x = [0,0,-1,1,-1,1,-1,1]
    for i in position:
        v = board[i[0]][i[1]]
        print(v)
        cnt = 0
        for j in range(len(x)):
            if (i[0]+y[j])>=0 and (i[0]+y[j])<y_max and (i[1]+x[j])>=0 and (i[1]+x[j])<x_max:
                cnt+=board[i[0]+y[j]][i[1]+x[j]]
        if v==1:
            if cnt<=2 or cnt>=5:
                answer.append(0)
            else:
                answer.append(v)
        else:
            if cnt==2:
                answer.append(1)
            else:
                answer.append(v)
        
    return answer
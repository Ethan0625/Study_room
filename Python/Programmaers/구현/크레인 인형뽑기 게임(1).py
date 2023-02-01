def solution(board, moves):
    '''if list[-1]==input:
        list.pop()
        answer+=2
        else:
        list.append(input)'''
    
    bucket=[]
    answer=0
    for i in moves:
        for j in range(len(board)):
            chk=board[j][i-1]
            if chk!=0:
                if len(bucket)!=0:
                    if bucket[-1]==chk:
                        board[j][i-1]=0
                        bucket.pop()
                        answer+=2
                    else :
                        bucket.append(chk)
                        board[j][i-1]=0
                else :
                    bucket.append(chk)
                    board[j][i-1]=0
                break
    
    return answer
def solution(brown, yellow):
    '''
    가로는 한줄
    한줄로 만들 수 있는 최대값
    '''
    answer = []
    for i in range(1,yellow+1):
        row = (yellow//i)+2
        
        if row*2+i*2==brown and yellow%i==0:
            return [row,i+2]
    return answer
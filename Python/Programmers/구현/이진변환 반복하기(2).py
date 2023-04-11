def solution(s):
    zero_sum = 0
    cnt = 0
    answer = []
    while s!='1':
        zero_cnt,s = s.count('0'),s.count('1')
        s = format(int(s),'b')
        zero_sum+=zero_cnt
        cnt+=1
    answer=[cnt,zero_sum]
    return answer
def solution(name):
    '''
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 24 25 26
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10  9  8  7  6  5  4  3  2  1
    a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    푸는중
    '''
    answer = 0
    print(name)
    loc_cnt = len(name)-1
    for i,s in enumerate(name):
        stick_cnt = ord(s)-65
        if stick_cnt>13:
            stick_cnt = stick_cnt-((stick_cnt-13)*2)
        answer += stick_cnt
        loc_cnt = min(loc_cnt,)
        
    # for i in name[1:]:
    #     if i!='A':
    #         answer += 1
    print(len(name))
    for j in range(1,len(name)):
        print(name[j])
        print(name[j+1:].count('A'))
        print('len(name[:j]) :',len(name[:j]))
        print('len(name[j+1:]) :',len(name[j+1:]))
    
    return answer
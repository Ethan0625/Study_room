def solution(s):
    '''
    n개 단위로 자른다
    
    '''
    result = []
    if len(s)==1:
        return 1
    # n개 단위로 자르는데 최대값은 문자열 길이의 반
    for i in range(1, (len(s) // 2)+1):
        c = '' # n개 단위로 자르면서 결과로 만들 문자열
        cnt = 1 # 연속된 문자열을 확인했을 때 붙이게 될 숫자, 기본값은 1
        s_char = s[:i] #잘라진 문자열
        
        # 잘라진 문자열 길이를 기준으로 반복문이 돌게 됨
        for j in range(i,len(s),i):
            if s_char==s[j:j+i]: # window만큼 이동
                cnt+=1
            else:
                if cnt==1:
                    c +=s_char
                else:
                    c+= str(cnt)+s_char
                cnt = 1
                s_char = s[j:j+i]
        
        # j 반복문이 끝났지만 단위로 잘라내어 압축한 마지막 부분은 반영되지 않음
        # 해당 부분 반영
        if cnt!=1:
            c += str(cnt) + s_char
        else:
            c += s_char
            
        result.append(len(c))
    return min(result)
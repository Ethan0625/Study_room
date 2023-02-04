def divide(p):
    if p=='':
        return p,p
    n = len(p)
    open_cnt = 0
    close_cnt = 0
    for i in range(n):
        if p[i]=='(':
            open_cnt+=1
        else:
            close_cnt+=1
        if open_cnt==close_cnt:
            return p[:i+1],p[i+1:]
def chk(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True

def solution(p):
    '''
    '('로 시작하는 palindrum
    '''
    # 1단계
    if p=='':
        return p
    # 2단계
    u,v = divide(p)
    # 3단계
    if chk(u):
        # 3-1단계
        return u + solution(v)
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        u = u[1:-1]
        for j in range(len(u)):
            if u[j]=='(':
                answer+=")"
            else:
                answer+="("
    return answer
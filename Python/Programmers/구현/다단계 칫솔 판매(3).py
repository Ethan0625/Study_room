def solution(enroll, referral, seller, amount):
    # dictionary를 활용하여 트리를 구현한다.
    # 트리를 계속 타고 올라가 Center가 나올때까지 확인
    # zip과 enumerate의 활용이 point
    money = [0 for _ in range(len(enroll))]
    dict = {}
    for i, e in enumerate(enroll):
        dict[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = dict[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]
    return money
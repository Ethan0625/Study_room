'''
[PCCE 모의고사 2] 9번
문제 설명
A회사의 사원들에게는 01100103와 같은 일련번호가 주어집니다. 일련번호는 8자리이며 순서대로 두 자리씩 성별, 소속 부서, 소속 팀, 유효성 번호로 구성되어 있습니다.

각 정보는 다음과 같습니다.

성별
male : 01
female : 02
소속 부서
operation : 10
sales : 11
develop : 12
finance : 13
law : 14
research : 15
소속 팀
Nteam : N
유효성 번호
valid: 유효성 번호를 제외한 6개의 숫자들을 모두 더해 13으로 나눈 나머지가 유효성 번호와 같을 때
invalid: 유효성 번호를 제외한 6개의 숫자들을 모두 더해 13으로 나눈 나머지가 유효성 번호와 다를 때
일련번호를 해석하는 방법은 다음과 같습니다.

1 단계. 일련번호를 앞에서부터 두 자리씩 끊어 저장합니다.
2 단계. 각 자리별로 위의 정보와 비교하여 문자열로 변경합니다.
예를 들어 일련번호가 01100103이면 male, operation, 1team이고 유효성 번호가 나머지 6개의 숫자를 모두 더한 (0 + 1 + 1 + 0 + 0 + 1 = 3)을 13으로 나눈 나머지 (3 % 13 = 3)과 같기 때문에 valid입니다. 그리고 이 정보를 "/"로 구분한 문자열로 나타내면 "male/operation/1team/valid"가 됩니다.

일련번호가 저장된 문자열 serial이 주어질 때 일련번호를 해석한 정보를 담은 문자열을 return 하도록 solution 함수를 완성해 보세요.
'''
def solution(serial):
    sex = {'01':'male','02':'female'}
    part =  {'10':'operation',
             '11':'sales',
             '12':'develop',
             '13':'finance',
             '14':'law',
             '15':'research',
            }
    sex_key = serial[:2]
    part_key = serial[2:4]
    team = int(serial[4:6])
    valid_str = serial[:6]
    valid_key = int(serial[-2:])
    chk_valid = 0
    for i in valid_str:
        chk_valid+=int(i)
    if chk_valid%13==valid_key:
        valid_status = 'valid'
    else:
        valid_status = 'invalid'

    answer = sex[sex_key]+'/'+part[part_key]+'/'+str(team)+'team'+'/'+valid_status
    return answer
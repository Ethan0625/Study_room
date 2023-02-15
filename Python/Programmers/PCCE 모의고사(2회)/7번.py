'''
[PCCE 모의고사 2] 7번
문제 설명
"0 10 123 45 678"과 같은 문자열이 주어질 때, 이를 "010-1234-5678"과 같은 전화번호 형식 문자열로 바꾸려 합니다. 문자열 입력이 저장된 phone과 다음 함수들이 주어질 때 이를 적절하게 호출하여 "010-XXXX-XXXX"(X는 숫자)와 같은 형식의 문자열을 return하는 함수를 완성해 주세요.

func1(msg) : msg의 글자 수를 세는 함수
func2(msg) : msg가 숫자로만 이루어져 있는지 확인하는 함수
func3(msg) : msg에 영어가 존재하는지 확인하는 함수
func4(msg) : msg에서 공백을 모두 제거하는 함수
func5(msg) : msg의 3번째, 7번째 자리에 -을 삽입하는 함수
단, 문자열 phone이 다음 조건을 만족하지 않는다면 "잘못된 입력입니다"를 return해야 합니다.

phone에 11개의 숫자가 포함되어있습니다.
phone는 숫자와 공백만으로 이루어져 있습니다.
'''

def func1(msg):
    return len(msg)

def func2(msg):
    for letter in msg:
        if '0' <= letter <= '9':
            continue
        return False
    return True

def func3(msg):
    for letter in msg:
        if 'a' <= letter <= 'z':
            return True
        if 'A' <= letter <= 'Z':
            return True
    return False

def func4(msg):
    while(" " in msg):
        msg = msg.replace(" ", "")
    return msg

def func5(msg):
    return msg[:3] + "-" + msg[3:7] + "-" + msg[7:]

def solution(phone):
    # 빈칸 채우기 문제
    phone = func4(phone)

    if not func2(phone) :
        return "잘못된 입력입니다"

    if func1(phone) != 11:
        return "잘못된 입력입니다"

    phone = func5(phone)
    # 빈칸 채우기 문제

    return phone
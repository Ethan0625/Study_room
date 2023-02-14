'''
[PCCE 모의고사 1] 5번
문제 설명
다음과 같이 다양한 기능을 하는 함수들이 정의되어 있습니다.

func1 : 매개변수 a를 입력받아 a * a를 return합니다.
func2 : 매개변수 a를 입력받아 a의 절댓값을 return합니다.
func3 : 매개변수 a와 b를 입력받아 a - b를 return합니다.
func4 : 매개변수 a와 b를 입력받아 a % (b의 절댓값)을 return합니다.
두 수 num1과 num2가 입력으로 주어질 때, 각각의 변수에 다음과 같은 값을 저장하도록 빈칸을 채워주세요.

answer_mod : num1을 num2의 절댓값으로 나눈 나머지
answer_pow : num1의 제곱 값
answer_abs : num2의 절댓값
알맞게 빈칸을 채울 경우 다음과 같이 출력됩니다.

입력

4
3
출력

num1을 num2의 절댓값으로 나눈 나머지는 1 입니다
num1의 제곱 값은 16 입니다
num2의 절댓값은 3 입니다
'''

def func1(a):
    return a * a

def func2(a):
    if a < 0 :
        return -1 * a
    return a

def func3(a, b):
    return a - b

def func4(a, b):
    if b > 0:
        return a % b
    return a % (-1 * b)


num1 = int(input())
num2 = int(input())

# 문제 구간
answer_mod = func4(num1,num2)

answer_pow = func1(num1)

answer_abs = func2(num2)
# 문제 구간

print("num1을 num2의 절댓값으로 나눈 나머지는", answer_mod, "입니다")
print("num1의 제곱 값은", answer_pow, "입니다")
print("num2의 절댓값은", answer_abs, "입니다")

'''
[PCCE 모의고사 2] 6번
문제 설명
주어진 solution 함수는 정수 n을 매개 변수로 받아 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, . . . n번째 줄에는 별 n개를 출력하는 함수입니다. 올바르게 작동하도록 한 줄을 수정해 보세요.
'''

def solution(n):
    # 기존 range(n)
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print()
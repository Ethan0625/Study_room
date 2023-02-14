'''
문제 설명
다음은 정수형 배열 num_list를 입력받아 배열의 원소가 홀수라면 "odd"를, 짝수라면 "even"를 answer에 저장하여 return하는 코드입니다. 단 "even"를 3번 저장한 경우 함수를 종료하려고 합니다. 코드를 한 줄만 수정해 정상적으로 작동되게 만들어주세요.
'''
# 디버깅 후
def solution(num_list):
    count_even = 0
    answer = []
    
    for num in num_list:
        if num % 2 == 0:
            answer.append("even")
            count_even += 1
            
            # 3번 저장한 이후라 사실 ==로 처리해도 됨
            if count_even >= 3:
                break
        else:
            answer.append("odd")
    
    return answer
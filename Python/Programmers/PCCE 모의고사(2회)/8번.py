'''
[PCCE 모의고사 2] 8번
문제 설명
주어진 초기 코드는 버블 정렬을 구현한 함수입니다. 버블 정렬이란 가장 큰 원소를 리스트의 맨 뒤로 보내며 정렬하는 방법을 말합니다.

버블 정렬은 다음과 같이 구현됩니다.

1 단계. 0부터 리스트의 길이 - 1까지 반복합니다.
    1-1 단계. i를 0부터 리스트의 길이 - 2까지 반복합니다.
        1-1-a 단계. 리스트의 i번째 원소가 i + 1번째 원소보다 크다면 두 원소의 위치를 바꿉니다.
        1-1-b 단계. 리스트의 i번째 원소가 i + 1번째 원소보다 작다면 두 원소의 위치를 바꾸지 않습니다.


정수들이 담긴 리스트 num_list가 주어질 때, 버블 정렬을 구현한 함수 solution이 올바르게 수행되도록 빈칸을 채워 보세요.
'''
def solution(num_list):
    for n in range(len(num_list)):
        for i in range(len(num_list)-1):
            if num_list[i]>num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]

    return num_list
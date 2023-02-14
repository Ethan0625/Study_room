'''
[PCCE 모의고사 1] 6번
문제 설명
주어진 초기 코드는 정수들이 저장된 리스트 num_list의 각 원소 값 만큼 반복해서 그 값을 출력하는 코드입니다.

예를들어 num_list가 [1, 4, 3]라면

1
4 4 4 4
3 3 3
으로 출력돼야 합니다.

올바르게 동작하도록 코드를 한 줄 수정해 보세요.
'''

num_list = [1, 3, 5, 2, 12]

for i in range(len(num_list)):
    # 기존 range(i)에서 수정
    # i만 하게 되면 0부터 시작하는 별찍기가 됨
    for j in range(num_list[i]):
        print(num_list[i], end=' ')
    print()
'''
[PCCE 모의고사 1] 7번
문제 설명
0부터 9까지의 정수가 담긴 리스트 num_list가 주어질 때, 길이가 10인 0으로 이루어진 리스트 count_list에 num_list에 저장된 원소들의 빈도수를 저장하려고 합니다.

num_list에 정수i가 있다면, count_list[i]에 1을 증가시켜 빈도수를 저장하면 됩니다.

만약 num_list가 [1, 1, 5, 2]라면 count_list는 [0, 2, 1, 0, 0, 1, 0, 0, 0, 0]가 됩니다.

코드가 올바르게 동작하도록 한 줄을 수정해 보세요.
'''

num_list = [9, 2, 3, 1, 6, 8, 0, 
            8, 9, 2, 1, 7, 7, 3, 5]

count_list = [0] * 10

for i in range(len(num_list)):
    # 기존 count_list[i]에서 변경
    # 단순 i를 하게 되면 0부터 시작하게 됨
    count_list[num_list[i]] += 1

# 출력 코드
print(count_list)
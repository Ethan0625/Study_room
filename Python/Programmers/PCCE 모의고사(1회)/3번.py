'''
[PCCE 모의고사 1] 3번
문제 설명
10부터 100까지의 수 중 짝수만 더한 값은 2530입니다. print(answer)의 출력 값이 2530이 되도록 빈칸을 채워 코드를 완성해 보세요
'''
answer = 0

for num in range(10,101,2):
    answer += num

print(answer)
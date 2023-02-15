'''
[PCCE 모의고사 2] 3번
문제 설명
주어진 초기 코드는 score에 저장된 점수에 따라 성적을 출력하는 코드입니다.

성적은 다음과 같이 매겨집니다.

90점 이상 - A
80점 이상 90점 미만 - B
70점 이상 80점 미만 - C
60점 이상 70점 미만 - D
60점 미만 - F
성적이 올바르게 출력되도록 빈칸을 채워보세요.
'''
score = int(input())

if score >= 90:
    print('A'
          )
elif score<90 and score>=80:
    print("B")
    
elif score<80 and score>=70:
    print("C")
    
elif score<70 and score>=60:
    print("D")
    
else:
    print("F")
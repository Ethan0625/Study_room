# SELCET
# https://programmers.co.kr/learn/courses/30/parts/17042
# 모든 레코드 조회하기
SELECT * FROM ANIMAL_INS;

# 역순 정렬하기
SELECT NAME, DATETIME FROM ANIMAL_INS ORDER BY ANIMAL_ID DESC;

# 아픈 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION = 'Sick';

# 어린 동물 찾기
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != 'Aged';

# 동물의 아이디와 이름
# 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문 작성
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS ORDER BY ANIMAL_ID;

# 여러 기준으로 정렬하기
# 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 
# 이름 순으로 조회하는 SQL문 작성
SELECT ANIMAL_ID, NAME, DATETIME 
FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC;

# 상위 N개 레코드
# 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회 하는 SQL문 작성
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1;
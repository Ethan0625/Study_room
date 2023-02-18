import itertools
import math
def is_prime(num):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(num)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if num % i == 0:
            return False # 소수가 아님
    return True

def solution(numbers):
    answer = set()
    numbers = [n for n in numbers]
    num_list = []
    for i in range(1,len(numbers)+1):
        tmp_list = list(set(list(itertools.permutations(numbers, i))))
        num_list+=tmp_list
    for j in num_list:
        chk_number = int(''.join(j))
        if chk_number!=1 and chk_number!=0:
            if is_prime(chk_number):
                answer.update([chk_number])
    return len(answer)
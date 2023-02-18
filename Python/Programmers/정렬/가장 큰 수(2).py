def solution(numbers):
    '''
    길이가 다름
    numbers의 최대 길이는 1000
    즉, 숫자를 반복하여 세자리수로 만들고 이를 기준으로 정렬하여 붙이면 됨
    
    '''
    numbers = list(map(str, numbers))
    # print('str_numbers :',numbers)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # print([i*3 for i in numbers])
    # print(numbers)
    return str(int(''.join(numbers)))
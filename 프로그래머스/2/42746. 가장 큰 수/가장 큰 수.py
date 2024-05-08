def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))
    # 문자열을 정렬하는 기준을 재정의하여 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)  # x*3을 하는 이유는 최대 1000이기 때문
    
    # 0이 여러 개 있는 경우 예외 처리
    if numbers[0] == '0':
        return '0'
    
    # 문자열을 이어붙여서 반환
    return ''.join(numbers)
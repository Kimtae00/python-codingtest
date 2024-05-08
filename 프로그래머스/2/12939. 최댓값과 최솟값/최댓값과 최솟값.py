def solution(s):
    # 문자열을 공백을 기준으로 분리하여 리스트로 변환
    numbers = list(map(int, s.split()))
    # 최소값과 최대값을 찾아 문자열로 변환하여 반환
    return f"{min(numbers)} {max(numbers)}"